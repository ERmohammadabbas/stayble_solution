from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order, OrderItem
import razorpay
import os
import json

client = razorpay.Client(auth=(os.environ.get('RAZORPAY_KEY_ID', ''), os.environ.get('RAZORPAY_KEY_SECRET', '')))

def home(request):
    featured_products = Product.objects.all()[:6]
    return render(request, 'shop/home.html', {'products': featured_products})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    
    product_id = str(pk)
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'title': product.title,
            'price': str(product.price),
            'quantity': 1,
            'image': product.image.url if product.image else ''
        }
    
    request.session['cart'] = cart
    messages.success(request, f'{product.title} added to cart!')
    return redirect('product_detail', pk=pk)

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    
    for product_id, item in cart.items():
        subtotal = float(item['price']) * item['quantity']
        cart_items.append({
            'id': product_id,
            'title': item['title'],
            'price': float(item['price']),
            'quantity': item['quantity'],
            'subtotal': subtotal,
            'image': item['image']
        })
        total += subtotal
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'shop/cart.html', context)

def update_cart(request, pk):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        
        product_id = str(pk)
        if product_id in cart:
            if quantity > 0:
                cart[product_id]['quantity'] = quantity
            else:
                del cart[product_id]
        
        request.session['cart'] = cart
        messages.success(request, 'Cart updated!')
    
    return redirect('cart')

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    product_id = str(pk)
    
    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart
        messages.success(request, 'Item removed from cart!')
    
    return redirect('cart')

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, 'Your cart is empty!')
        return redirect('product_list')
    
    cart_items = []
    total = 0
    
    for product_id, item in cart.items():
        subtotal = float(item['price']) * item['quantity']
        cart_items.append({
            'id': product_id,
            'title': item['title'],
            'price': float(item['price']),
            'quantity': item['quantity'],
            'subtotal': subtotal
        })
        total += subtotal
    
    if request.method == 'POST':
        razorpay_key_id = os.environ.get('RAZORPAY_KEY_ID', '')
        razorpay_key_secret = os.environ.get('RAZORPAY_KEY_SECRET', '')
        
        if not razorpay_key_id or not razorpay_key_secret:
            messages.warning(request, 'Razorpay is not configured. Please set RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET.')
            return redirect('checkout')
        
        try:
            amount = int(total * 100)
            razorpay_order = client.order.create({
                'amount': amount,
                'currency': 'INR',
                'payment_capture': 1
            })
            
            order = Order.objects.create(
                user=request.user,
                total_amount=total,
                razorpay_order_id=razorpay_order['id']
            )
            
            for product_id, item in cart.items():
                product = Product.objects.get(pk=int(product_id))
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                    price=item['price']
                )
            
            context = {
                'order': order,
                'razorpay_key_id': razorpay_key_id,
                'razorpay_order_id': razorpay_order['id'],
                'amount': amount,
                'cart_items': cart_items,
                'total': total
            }
            return render(request, 'shop/payment.html', context)
        except Exception as e:
            messages.error(request, f'Payment setup failed: {str(e)}')
            return redirect('checkout')
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'shop/checkout.html', context)

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        
        razorpay_payment_id = data.get('razorpay_payment_id')
        razorpay_order_id = data.get('razorpay_order_id')
        razorpay_signature = data.get('razorpay_signature')
        
        if not all([razorpay_payment_id, razorpay_order_id, razorpay_signature]):
            return JsonResponse({'status': 'error', 'message': 'Missing payment parameters'}, status=400)
        
        try:
            order = Order.objects.get(razorpay_order_id=razorpay_order_id)
            
            if order.is_paid:
                return JsonResponse({'status': 'error', 'message': 'Order already paid'}, status=400)
            
            razorpay_key_secret = os.environ.get('RAZORPAY_KEY_SECRET', '')
            if not razorpay_key_secret:
                return JsonResponse({'status': 'error', 'message': 'Payment system misconfigured'}, status=500)
            
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            
            try:
                import hmac
                import hashlib
                
                generated_signature = hmac.new(
                    razorpay_key_secret.encode('utf-8'),
                    f"{razorpay_order_id}|{razorpay_payment_id}".encode('utf-8'),
                    hashlib.sha256
                ).hexdigest()
                
                if generated_signature != razorpay_signature:
                    return JsonResponse({'status': 'error', 'message': 'Invalid payment signature'}, status=400)
                
                order.razorpay_payment_id = razorpay_payment_id
                order.razorpay_signature = razorpay_signature
                order.is_paid = True
                order.save()
                
                request.session['cart'] = {}
                
                return JsonResponse({'status': 'success', 'order_id': order.id})
                
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': 'Payment verification failed'}, status=400)
                
        except Order.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Order not found'}, status=404)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_confirmation.html', {'order': order})
