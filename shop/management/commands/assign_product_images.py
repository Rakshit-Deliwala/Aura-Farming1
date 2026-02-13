"""
Download placeholder images and assign them to each product.
Uses Picsum (picsum.photos) for free placeholder images.
Run: python manage.py assign_product_images
"""
import urllib.request
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    help = "Download placeholder images and assign to each product."

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Re-download and overwrite even if product already has an image.",
        )

    def handle(self, *args, **options):
        media_root = Path(settings.MEDIA_ROOT)
        products_dir = media_root / "products"
        products_dir.mkdir(parents=True, exist_ok=True)

        products = Product.objects.all().order_by("id")
        if not products.exists():
            self.stdout.write(self.style.WARNING("No products found. Create products first."))
            return

        for product in products:
            if product.image and not options["force"]:
                self.stdout.write(f"  Skipping '{product.name}' (already has image).")
                continue

            filename = f"product-{product.id}.jpg"
            filepath = products_dir / filename
            # Picsum: seed by product id so each product gets a consistent image
            url = f"https://picsum.photos/seed/aura{product.id}/400/300"

            try:
                urllib.request.urlretrieve(url, filepath)
                # Save path relative to MEDIA_ROOT (e.g. "products/product-1.jpg")
                product.image = f"products/{filename}"
                product.save()
                self.stdout.write(self.style.SUCCESS(f"  Assigned image to: {product.name}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  Failed for '{product.name}': {e}"))

        self.stdout.write(self.style.SUCCESS("Done."))
