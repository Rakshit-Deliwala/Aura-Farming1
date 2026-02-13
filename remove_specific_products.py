import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import Product

# List of products to remove
products_to_remove = [
    "Kids Gardening Tool Set (6-in-1)",
    "Stainless Steel Hand Trowel",
    "Pruning Secateurs - Professional Grade",
    "Vertical Wall Planter Set (6 pockets)",
    "Drip Irrigation Kit for 25 Plants",
    "Garden Kneeler & Seat 2-in-1",
    "Compost Bin - 50L Capacity",
    "Herb Garden Kit - Kitchen Essentials",
    "Mushroom Growing Kit - Oyster Variety",
    "Cactus & Succulent Garden Kit"
]

print(f"Total products before deletion: {Product.objects.count()}")
print("\nSearching for products to delete...\n")

deleted_count = 0
not_found = []

for product_name in products_to_remove:
    try:
        product = Product.objects.get(name=product_name)
        print(f"✓ Found and deleting: {product.name}")
        product.delete()
        deleted_count += 1
    except Product.DoesNotExist:
        print(f"✗ Not found: {product_name}")
        not_found.append(product_name)

print(f"\n{'='*60}")
print(f"✓ Successfully deleted {deleted_count} products")
print(f"✗ Not found: {len(not_found)} products")
print(f"Remaining products: {Product.objects.count()}")
print(f"{'='*60}")

if not_found:
    print("\nProducts not found in database:")
    for name in not_found:
        print(f"  - {name}")
