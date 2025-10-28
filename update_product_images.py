import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from shop.models import Product

# Mapping of product IDs to image filenames
product_images = {
    1: 'products/wireless_bluetooth_h_34934def.jpg',
    2: 'products/smart_watch_fitness__c5727610.jpg',
    3: 'products/laptop_backpack_mode_7f7afe1a.jpg',
    4: 'products/portable_power_bank__a4042d94.jpg',
    5: 'products/mechanical_gaming_ke_2abe121d.jpg',
    6: 'products/wireless_gaming_mous_9977e78a.jpg',
    7: 'products/usb-c_hub_multiport__c37328e1.jpg',
    8: 'products/wireless_earbuds_blu_a240c162.jpg',
    9: 'products/phone_stand_wireless_7a0f7047.jpg',
    10: 'products/hd_webcam_1080p_stre_e8c344e1.jpg',
}

print("Updating product images...")
for product_id, image_path in product_images.items():
    try:
        product = Product.objects.get(id=product_id)
        product.image = image_path
        product.save()
        print(f"✓ Updated {product.title} with image: {image_path}")
    except Product.DoesNotExist:
        print(f"✗ Product with ID {product_id} not found")

print("\nVerifying updates...")
products = Product.objects.all()
for product in products:
    print(f"{product.id}: {product.title} - Image: {product.image}")

print("\nAll product images have been updated successfully! 🎉")
