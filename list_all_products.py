import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import Product, Category

print("=" * 80)
print("AURA FARMING - Complete Product Catalog (86 Products)")
print("=" * 80)
print()

for category in Category.objects.all():
    products = Product.objects.filter(category=category).order_by('name')
    print(f"\n{'='*80}")
    print(f"📦 {category.name.upper()} ({products.count()} products)")
    print(f"{'='*80}")
    
    for i, product in enumerate(products, 1):
        stock_status = "✅ In Stock" if product.stock > 20 else "⚠️ Low Stock" if product.stock > 0 else "❌ Out of Stock"
        featured = "⭐" if product.is_featured else "  "
        
        print(f"{featured} {i:2d}. {product.name}")
        print(f"      Price: ₹{product.price_inr:,} | Stock: {product.stock} | {stock_status}")
        if product.tags:
            print(f"      Tags: {product.tags}")
        print()

print("=" * 80)
print(f"Total: {Product.objects.count()} products across {Category.objects.count()} categories")
print("=" * 80)
