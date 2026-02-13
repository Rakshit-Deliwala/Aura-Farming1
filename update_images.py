"""
Standalone script to update product images in database
Run with: python update_images.py
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import Product

# Image mapping
image_mapping = {
    'AURA Premium Gardening Toolkit (8-in-1)': 'products/gardening-toolkit.jpg',
    'Beginner Balcony Farming Kit': 'products/balcony-farming-kit.jpg',
    'Microgreens DIY Kit – 5 Varieties': 'products/microgreens-kit.jpg',
    'Organic Vegetable Potting Mix 10kg': 'products/potting-mix.jpg',
    'Rakhi Eco-Gift Hamper with Plantable Seeds': 'products/rakhi-eco-gift.jpg',
    'Corporate Desk Garden Gift Box': 'products/corporate-desk-garden.jpg',
}

print("Updating product images in database...\n")

updated_count = 0
for product_name, image_path in image_mapping.items():
    try:
        product = Product.objects.get(name=product_name)
        product.image = image_path
        product.save()
        print(f"✓ Updated: {product_name}")
        updated_count += 1
    except Product.DoesNotExist:
        print(f"✗ Product not found: {product_name}")

print(f"\n✅ Successfully updated {updated_count} products with images!")
print("🌐 Refresh your browser to see the images on the website")
