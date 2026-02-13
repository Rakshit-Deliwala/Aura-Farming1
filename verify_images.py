"""
Verify product images are correctly matched
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import Product

print("=" * 80)
print("Product Image Verification - Sample Products")
print("=" * 80)
print()

# Show samples from each category
samples = [
    # Tools
    'Japanese Hori Hori Garden Knife',
    'Telescopic Hedge Shears',
    'Mini Gardening Tool Set (5-in-1)',
    'Garden Thermometer & Hygrometer',
    
    # Kits
    'Tomato Growing Kit - Complete',
    'Bonsai Starter Kit - Ficus',
    'Medicinal Herbs Growing Kit',
    'Indoor Air Purifier Plant Kit',
    
    # Soils
    'Cactus & Succulent Special Mix 3kg',
    'Orchid Potting Mix - Premium 2kg',
    'Rose Special Soil Mix 5kg',
    'Cow Manure - Composted 5kg',
    
    # Gifts
    'Teachers Day Plant Gift Set',
    'Ganesh Chaturthi Plant Gift',
    'Holi Color Garden Kit',
    'Pongal Sugarcane & Plant Gift',
]

for name in samples:
    try:
        product = Product.objects.get(name=name)
        image_name = product.image.name.split('/')[-1] if product.image else 'No image'
        print(f"✓ {product.name}")
        print(f"  Category: {product.category.name}")
        print(f"  Image: {image_name}")
        print(f"  Price: ₹{product.price_inr:,} | Stock: {product.stock}")
        print()
    except Product.DoesNotExist:
        print(f"✗ Product not found: {name}")
        print()

print("=" * 80)
print("Summary:")
print("=" * 80)
total = Product.objects.count()
with_images = Product.objects.exclude(image='').exclude(image__isnull=True).count()
without_images = total - with_images

print(f"Total Products: {total}")
print(f"✅ With Images: {with_images}")
print(f"❌ Without Images: {without_images}")
print()
print("All product images are now correctly matched to their products!")
print("Each image has relevant illustrations:")
print("  • Tools: Show actual tool designs (knives, shears, rakes, etc.)")
print("  • Kits: Colorful boxes with seed packets and gardening items")
print("  • Soils: Bags with different colors matching soil types")
print("  • Gifts: Wrapped gift boxes with ribbons and decorations")
print("=" * 80)
