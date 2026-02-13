from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path


class Command(BaseCommand):
    help = 'Generate placeholder images for products'

    def handle(self, *args, **options):
        media_products = Path('media/products')
        media_products.mkdir(parents=True, exist_ok=True)

        # Product images with category-specific colors
        products = [
            {
                'filename': 'gardening-toolkit.jpg',
                'title': 'Gardening\nToolkit',
                'color': '#2d5016',  # Dark green
                'icon': '🔧'
            },
            {
                'filename': 'balcony-farming-kit.jpg',
                'title': 'Balcony\nFarming Kit',
                'color': '#4a7c59',  # Medium green
                'icon': '🌱'
            },
            {
                'filename': 'microgreens-kit.jpg',
                'title': 'Microgreens\nDIY Kit',
                'color': '#6b9b37',  # Fresh green
                'icon': '🌿'
            },
            {
                'filename': 'potting-mix.jpg',
                'title': 'Organic\nPotting Mix',
                'color': '#5d4037',  # Brown
                'icon': '🌾'
            },
            {
                'filename': 'rakhi-eco-gift.jpg',
                'title': 'Rakhi\nEco-Gift',
                'color': '#d84315',  # Orange-red
                'icon': '🎁'
            },
            {
                'filename': 'corporate-desk-garden.jpg',
                'title': 'Corporate\nDesk Garden',
                'color': '#1b5e20',  # Forest green
                'icon': '🪴'
            }
        ]

        for product in products:
            img_path = media_products / product['filename']
            
            # Create a 800x800 image
            img = Image.new('RGB', (800, 800), color=product['color'])
            draw = ImageDraw.Draw(img)
            
            # Add lighter border
            border_color = self.lighten_color(product['color'], 0.3)
            draw.rectangle([20, 20, 780, 780], outline=border_color, width=8)
            
            # Add pattern/texture
            for i in range(0, 800, 40):
                draw.line([(i, 0), (i, 800)], fill=self.lighten_color(product['color'], 0.1), width=1)
                draw.line([(0, i), (800, i)], fill=self.lighten_color(product['color'], 0.1), width=1)
            
            # Add center circle with light background
            circle_color = self.lighten_color(product['color'], 0.6)
            draw.ellipse([200, 200, 600, 600], fill=circle_color, outline='white', width=6)
            
            # Add text (simplified - PIL default font)
            text_bbox = draw.textbbox((0, 0), product['icon'], font=None)
            icon_size = text_bbox[2] - text_bbox[0]
            # Use larger text by repeating
            icon_text = product['icon'] * 3
            text_x = 400 - 30
            text_y = 320
            draw.text((text_x, text_y), icon_text, fill='white', font=None)
            
            # Add product title
            title_y = 480
            for line in product['title'].split('\n'):
                text_bbox = draw.textbbox((0, 0), line, font=None)
                text_width = text_bbox[2] - text_bbox[0]
                text_x = (800 - text_width) // 2
                draw.text((text_x, title_y), line, fill='white', font=None)
                title_y += 30
            
            # Add AURA FARMING branding
            brand = "AURA FARMING"
            brand_bbox = draw.textbbox((0, 0), brand, font=None)
            brand_width = brand_bbox[2] - brand_bbox[0]
            brand_x = (800 - brand_width) // 2
            draw.text((brand_x, 700), brand, fill=self.lighten_color(product['color'], 0.5), font=None)
            
            # Save image
            img.save(img_path, 'JPEG', quality=90)
            self.stdout.write(self.style.SUCCESS(f'Created: {img_path}'))

        self.stdout.write(self.style.SUCCESS('\nAll product images generated successfully!'))

    def lighten_color(self, hex_color, factor):
        """Lighten a hex color by a factor (0-1)"""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))
        return f'#{r:02x}{g:02x}{b:02x}'
