import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import Product, Category

print(f'✅ Total Products: {Product.objects.count()}')
print(f'📦 Total Categories: {Category.objects.count()}')
print('\n📊 Products by Category:')
for cat in Category.objects.all():
    count = cat.product_set.count()
    print(f'   • {cat.name}: {count} products')

print('\n🆕 Recently Added Products (last 10):')
for p in Product.objects.order_by('-id')[:10]:
    print(f'   • {p.name} - ₹{p.price_inr} (Stock: {p.stock})')
