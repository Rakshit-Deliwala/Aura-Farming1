import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import Product

def remove_products_without_images():
    """Remove all products that don't have image_url"""
    
    # Get all products
    all_products = Product.objects.all()
    total_count = all_products.count()
    
    # Get products with images
    products_with_images = Product.objects.filter(image_url__isnull=False).exclude(image_url='')
    keep_count = products_with_images.count()
    
    # Get products without images
    products_to_delete = Product.objects.filter(image_url__isnull=True) | Product.objects.filter(image_url='')
    delete_count = products_to_delete.count()
    
    print(f"Total products: {total_count}")
    print(f"Products with images (keeping): {keep_count}")
    print(f"Products without images (deleting): {delete_count}")
    print("\nProducts to keep:")
    for product in products_with_images:
        print(f"  ✓ {product.name}")
    
    print("\nProducts to delete:")
    for product in products_to_delete:
        print(f"  ✗ {product.name}")
    
    # Delete products
    print(f"\n{'='*60}")
    print(f"Deleting {delete_count} products...")
    deleted_count = products_to_delete.delete()[0]
    print(f"\n✓ Deleted {deleted_count} products successfully!")
    print(f"✓ Remaining products: {Product.objects.count()}")

if __name__ == '__main__':
    print("Product Cleanup Script")
    print("="*60)
    remove_products_without_images()
    print("\nDone!")
