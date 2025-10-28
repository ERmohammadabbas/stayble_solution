# E-Commerce Django Website

## Overview
A fully functional e-commerce web application built with Django, featuring user authentication, product management, shopping cart functionality, and Razorpay payment integration.

## Project Structure
```
ecommerce/          # Main Django project
├── settings.py     # Project settings
├── urls.py         # Main URL configuration
└── wsgi.py         # WSGI configuration

shop/               # Main shop application
├── models.py       # Product, Order, OrderItem models
├── views.py        # All shop views (product list, cart, checkout, etc.)
├── admin.py        # Admin panel configuration
└── urls.py         # Shop URL routes

accounts/           # User authentication application
├── views.py        # Login, register, logout views
└── urls.py         # Account URL routes

templates/          # HTML templates
├── base.html       # Base template with navigation
├── shop/           # Shop templates
│   ├── home.html
│   ├── product_list.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── checkout.html
│   ├── payment.html
│   └── order_confirmation.html
└── accounts/       # Account templates
    ├── login.html
    └── register.html

static/             # Static files
├── css/
│   └── style.css   # Custom CSS
└── js/             # JavaScript files

media/              # User-uploaded files
└── products/       # Product images
```

## Features Implemented

### 1. User Authentication
- User registration with username and password
- Login/Logout functionality
- Session management

### 2. Product Management
- Product model with image, title, description, price, stock
- Product listing page
- Product detail page with images
- Admin panel for adding/editing/deleting products

### 3. Shopping Cart
- Session-based cart (no login required for browsing)
- Add to cart functionality
- Update cart quantities
- Remove items from cart
- Real-time cart count in navigation

### 4. Checkout & Payment
- Checkout page with order summary
- Razorpay payment gateway integration (test mode)
- Payment success handling
- Order confirmation page with order details

### 5. Additional Pages
- Home page with featured products
- About page
- Contact page
- Responsive design using Bootstrap 5

## Technologies Used
- **Backend**: Django 5.2.7
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **Payment**: Razorpay SDK
- **Image Handling**: Pillow

## Admin Panel
Access the admin panel at `/admin/`:
- Username: `admin`
- Password: `admin123`

Use the admin panel to:
- Add new products with images
- Edit existing products
- Delete products
- View orders and order items
- Manage users

## Environment Variables Required

### Razorpay Configuration
To enable payment functionality, set these environment secrets:
- `RAZORPAY_KEY_ID` - Your Razorpay API Key ID
- `RAZORPAY_KEY_SECRET` - Your Razorpay API Secret

Get test API keys from: https://dashboard.razorpay.com/

## URL Routes
- `/` - Home page
- `/products/` - Product listing
- `/product/<id>/` - Product detail
- `/cart/` - Shopping cart
- `/checkout/` - Checkout page (requires login)
- `/about/` - About page
- `/contact/` - Contact page
- `/accounts/register/` - User registration
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/admin/` - Django admin panel

## How to Use

### Adding Products
1. Go to `/admin/` and login with admin credentials
2. Click on "Products" → "Add Product"
3. Fill in title, description, price, stock
4. Upload a product image
5. Click "Save"

### Making a Purchase
1. Browse products on the home page or products page
2. Click on a product to view details
3. Click "Add to Cart"
4. View cart and update quantities if needed
5. Click "Proceed to Checkout" (requires login)
6. Review order and click "Pay with Razorpay"
7. Complete payment using Razorpay (test mode)
8. View order confirmation

## Database Models

### Product
- title: Product name
- description: Product description
- price: Product price (decimal)
- image: Product image (ImageField)
- stock: Available quantity
- created_at: Timestamp

### Order
- user: Foreign key to User
- total_amount: Order total (decimal)
- razorpay_order_id: Razorpay order ID
- razorpay_payment_id: Razorpay payment ID
- razorpay_signature: Payment signature
- is_paid: Payment status (boolean)
- created_at: Timestamp

### OrderItem
- order: Foreign key to Order
- product: Foreign key to Product
- quantity: Item quantity
- price: Price at time of purchase

## Recent Changes
- October 27, 2025: Initial project setup with all features implemented
- Django e-commerce website created from scratch
- All 18 requirements fulfilled
- Admin panel configured
- Razorpay payment integration added
- Responsive design implemented

## Notes
- The application uses session-based cart storage (cart data is stored in user sessions)
- Payment gateway is configured for test mode
- Images are stored in the `media/products/` directory
- Static files (CSS, JS) are in the `static/` directory
- Bootstrap 5 is used for responsive design
