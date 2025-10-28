from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at']
    search_fields = ['user__username', 'razorpay_order_id']
    inlines = [OrderItemInline]
    readonly_fields = ['razorpay_order_id', 'razorpay_payment_id', 'razorpay_signature']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
