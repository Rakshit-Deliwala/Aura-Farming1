from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = 'Assign generated images to products'

    def handle(self, *args, **options):
        image_mapping = {
            'AURA Premium Gardening Toolkit (8-in-1)': 'products/gardening-toolkit.jpg',
            'Beginner Balcony Farming Kit': 'products/balcony-farming-kit.jpg',
            'Microgreens DIY Kit – 5 Varieties': 'products/microgreens-kit.jpg',
            'Organic Vegetable Potting Mix 10kg': 'products/potting-mix.jpg',
            'Rakhi Eco-Gift Hamper with Plantable Seeds': 'products/rakhi-eco-gift.jpg',
            'Corporate Desk Garden Gift Box': 'products/corporate-desk-garden.jpg',
        }

        for product_name, image_path in image_mapping.items():
            try:
                product = Product.objects.get(name=product_name)
                product.image = image_path
                product.save()
                self.stdout.write(self.style.SUCCESS(f'✓ Updated: {product_name}'))
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'✗ Product not found: {product_name}'))

        self.stdout.write(self.style.SUCCESS('\nProduct images updated successfully!'))
