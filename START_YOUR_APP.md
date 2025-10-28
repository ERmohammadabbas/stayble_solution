# 🚀 How to Start Your Django E-Commerce Application

Your application is ready with **10 unique product images**! Follow these simple steps to start it:

## Quick Start (Recommended)

### Option 1: Run from Shell Tab
1. Click on the **Shell** tab in Replit
2. Run this command:
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```
3. Click on the webview URL that appears to see your application

### Option 2: Use the Run Script
1. Open the **Shell** tab
2. Run:
   ```bash
   ./run_django.sh
   ```

## What You'll See

Once the server starts, your e-commerce application will display:

### Home Page (`/`)
- 🎨 Hero section with call-to-action buttons
- 📦 6 featured products - **each with a UNIQUE image**
- ✨ Features section (Free Shipping, Secure Payment, 24/7 Support)

### Products Page (`/products/`)
- 🛍️ All 10 products in a grid layout
- 🖼️ **Each product has its own DIFFERENT image**
- 📱 Fully responsive design

### Other Features
- 🔐 User Login/Register (`/accounts/login/`, `/accounts/register/`)
- 🛒 Shopping Cart (`/cart/`)
- 💳 Checkout & Payment with Razorpay (`/checkout/`)
- 📄 Product Detail Pages

## Product Images

All products now have unique, professional images:

1. ✅ Wireless Bluetooth Headphones - Sleek black headphones
2. ✅ Smart Watch Pro - Modern fitness tracker
3. ✅ Laptop Backpack - Professional travel bag
4. ✅ Portable Power Bank - Compact battery charger
5. ✅ Mechanical Gaming Keyboard - RGB keyboard
6. ✅ Wireless Gaming Mouse - Professional mouse
7. ✅ USB-C Hub - Multiport adapter
8. ✅ Wireless Earbuds Pro - Bluetooth earbuds
9. ✅ Phone Stand & Wireless Charger - Charging pad
10. ✅ HD Webcam 1080p - Streaming camera

## Troubleshooting

If port 5000 is already in use:
```bash
# Kill any process on port 5000
pkill -f "runserver" && pkill -f "tsx server"
# Then start Django
python manage.py runserver 0.0.0.0:5000
```

## Ready to Browse!

Your e-commerce store is fully functional with:
- ✅ Beautiful, unique product images
- ✅ Working shopping cart
- ✅ User authentication
- ✅ Payment integration (Razorpay)
- ✅ Responsive design

**Enjoy your updated e-commerce application!** 🎉
