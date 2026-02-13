"""
Generate all product images for AURA FARMING
Run with: python generate_all_images.py
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def lighten_color(hex_color, factor):
    """Lighten a hex color by a factor (0-1)"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = min(255, int(r + (255 - r) * factor))
    g = min(255, int(g + (255 - g) * factor))
    b = min(255, int(b + (255 - b) * factor))
    return (r, g, b)


def darken_color(hex_color, factor):
    """Darken a hex color by a factor (0-1)"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = int(r * (1 - factor))
    g = int(g * (1 - factor))
    b = int(b * (1 - factor))
    return (r, g, b)


def draw_icon(draw, icon_type, center_x, center_y, color):
    """Draw custom icon"""
    if isinstance(color, str):
        color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    lighter = tuple(min(255, int(c * 1.3)) for c in color)
    
    if icon_type == 'toolkit':
        draw.rectangle([center_x-60, center_y-10, center_x+60, center_y+10], fill=color)
        draw.ellipse([center_x-70, center_y-20, center_x-50, center_y+20], fill=color)
        draw.ellipse([center_x+50, center_y-20, center_x+70, center_y+20], fill=color)
        draw.rectangle([center_x-40, center_y-60, center_x-20, center_y-10], fill=color)
        draw.polygon([center_x-40, center_y-60, center_x-20, center_y-60, center_x-30, center_y-80], fill=color)
    elif icon_type == 'plant':
        draw.ellipse([center_x-15, center_y+20, center_x+15, center_y+50], fill=color)
        draw.rectangle([center_x-10, center_y, center_x+10, center_y+20], fill=color)
        draw.ellipse([center_x-40, center_y-20, center_x-10, center_y+10], fill=color)
        draw.ellipse([center_x+10, center_y-30, center_x+40, center_y], fill=color)
        draw.ellipse([center_x-25, center_y-40, center_x+5, center_y-10], fill=color)
    elif icon_type == 'sprout':
        for i in range(-30, 40, 20):
            draw.rectangle([center_x+i-3, center_y-40, center_x+i+3, center_y+20], fill=color)
            draw.ellipse([center_x+i-8, center_y-50, center_x+i+8, center_y-35], fill=color)
    elif icon_type == 'soil':
        draw.rectangle([center_x-50, center_y-20, center_x+50, center_y+50], fill=color)
        draw.polygon([center_x-50, center_y-20, center_x, center_y-40, center_x+50, center_y-20], fill=color)
        for y in range(-10, 40, 15):
            for x in range(-40, 45, 20):
                draw.ellipse([center_x+x-3, center_y+y-3, center_x+x+3, center_y+y+3], fill=lighter)
    elif icon_type == 'gift':
        draw.rectangle([center_x-50, center_y-30, center_x+50, center_y+40], fill=color)
        draw.rectangle([center_x-50, center_y-50, center_x+50, center_y-30], fill=lighter)
        draw.rectangle([center_x-5, center_y-50, center_x+5, center_y+40], fill='white')
        draw.rectangle([center_x-50, center_y-5, center_x+50, center_y+5], fill='white')
        draw.ellipse([center_x-20, center_y-70, center_x-5, center_y-50], fill='white')
        draw.ellipse([center_x+5, center_y-70, center_x+20, center_y-50], fill='white')
    elif icon_type == 'pot':
        draw.polygon([center_x-35, center_y+20, center_x-45, center_y+50, center_x+45, center_y+50, center_x+35, center_y+20], fill=color)
        draw.ellipse([center_x-25, center_y-10, center_x-5, center_y+20], fill='white')
        draw.ellipse([center_x+5, center_y-10, center_x+25, center_y+20], fill='white')
        draw.ellipse([center_x-12, center_y-25, center_x+12, center_y+5], fill='white')
    elif icon_type == 'mini-tools':
        draw.rectangle([center_x-30, center_y-5, center_x+30, center_y+5], fill=color)
        draw.ellipse([center_x-35, center_y-10, center_x-25, center_y+10], fill=color)
        draw.ellipse([center_x+25, center_y-10, center_x+35, center_y+10], fill=color)
    elif icon_type == 'kids':
        for i in range(-20, 30, 25):
            draw.ellipse([center_x+i-15, center_y-30, center_x+i+15, center_y], fill=color)
            draw.rectangle([center_x+i-5, center_y, center_x+i+5, center_y+40], fill=color)
    elif icon_type == 'flower':
        for angle in range(0, 360, 60):
            import math
            x = center_x + int(25 * math.cos(math.radians(angle)))
            y = center_y + int(25 * math.sin(math.radians(angle)))
            draw.ellipse([x-12, y-12, x+12, y+12], fill=color)
        draw.ellipse([center_x-12, center_y-12, center_x+12, center_y+12], fill=lighter)
    elif icon_type == 'leaf':
        draw.ellipse([center_x-35, center_y-15, center_x+5, center_y+35], fill=color)
        draw.ellipse([center_x-5, center_y-35, center_x+35, center_y+15], fill=color)


def create_product_image(filename, title, color, icon_type):
    """Create professional product image"""
    img = Image.new('RGB', (800, 800), color=color)
    draw = ImageDraw.Draw(img)
    
    # Gradient
    base_color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    for y in range(800):
        factor = y / 800 * 0.3
        gradient_color = darken_color(color, factor)
        draw.line([(0, y), (800, y)], fill=gradient_color, width=1)
    
    # Decorative corners
    corner_color = lighten_color(color, 0.2)
    for i in range(0, 100, 10):
        draw.arc([i, i, 200-i, 200-i], 180, 270, fill=corner_color, width=3)
        draw.arc([600+i, i, 800-i, 200-i], 270, 360, fill=corner_color, width=3)
        draw.arc([i, 600+i, 200-i, 800-i], 90, 180, fill=corner_color, width=3)
        draw.arc([600+i, 600+i, 800-i, 800-i], 0, 90, fill=corner_color, width=3)
    
    # Border
    border_color = lighten_color(color, 0.4)
    draw.rectangle([30, 30, 770, 770], outline=border_color, width=10)
    
    # White circle
    draw.ellipse([200, 200, 600, 600], fill='white', outline=lighten_color(color, 0.5), width=8)
    
    # Icon
    icon_color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    draw_icon(draw, icon_type, 400, 400, icon_color)
    
    # Text
    try:
        title_font = ImageFont.truetype("arial.ttf", 48)
        brand_font = ImageFont.truetype("arialbd.ttf", 32)
    except:
        title_font = ImageFont.load_default()
        brand_font = ImageFont.load_default()
    
    text_y = 640
    for line in title.split('\n'):
        bbox = draw.textbbox((0, 0), line, font=title_font)
        text_width = bbox[2] - bbox[0]
        text_x = (800 - text_width) // 2
        draw.text((text_x+2, text_y+2), line, fill=(0, 0, 0, 128), font=title_font)
        draw.text((text_x, text_y), line, fill='white', font=title_font)
        text_y += 55
    
    brand_text = "AURA FARMING"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    brand_width = bbox[2] - bbox[0]
    brand_x = (800 - brand_width) // 2
    draw.text((brand_x, 730), brand_text, fill=lighten_color(color, 0.6), font=brand_font)
    
    return img


# Create directory
media_dir = Path('media/products')
media_dir.mkdir(parents=True, exist_ok=True)

# All products
products = [
    # Toolkits
    {'filename': 'gardening-toolkit.jpg', 'title': 'Premium\nToolkit 8-in-1', 'color': '#2d5016', 'icon': 'toolkit'},
    {'filename': 'mini-tool-set.jpg', 'title': 'Mini Tool Set\n5-in-1', 'color': '#4a7c59', 'icon': 'mini-tools'},
    {'filename': 'professional-toolkit.jpg', 'title': 'Professional\nToolkit 12-in-1', 'color': '#1b5e20', 'icon': 'toolkit'},
    {'filename': 'kids-tool-set.jpg', 'title': 'Kids Gardening\nTool Set', 'color': '#ff9800', 'icon': 'kids'},
    {'filename': 'balcony-essentials.jpg', 'title': 'Balcony\nEssentials Kit', 'color': '#4a7c59', 'icon': 'plant'},
    {'filename': 'terrace-master-kit.jpg', 'title': 'Terrace\nMaster Kit', 'color': '#2d5016', 'icon': 'toolkit'},
    {'filename': 'bonsai-toolkit.jpg', 'title': 'Bonsai Care\nToolkit', 'color': '#5d4037', 'icon': 'leaf'},
    {'filename': 'organic-farming-kit.jpg', 'title': 'Organic\nFarming Kit', 'color': '#6b9b37', 'icon': 'sprout'},
    
    # Individual Tools
    {'filename': 'hand-trowel.jpg', 'title': 'Stainless Steel\nTrowel', 'color': '#757575', 'icon': 'mini-tools'},
    {'filename': 'pruning-secateurs.jpg', 'title': 'Pruning\nSecateurs', 'color': '#d84315', 'icon': 'mini-tools'},
    {'filename': 'garden-gloves.jpg', 'title': 'Anti-Cut\nGarden Gloves', 'color': '#ff9800', 'icon': 'leaf'},
    {'filename': 'watering-can.jpg', 'title': 'Watering Can\n5L Capacity', 'color': '#2196f3', 'icon': 'pot'},
    {'filename': 'soil-tester.jpg', 'title': 'Soil pH\nTester 3-in-1', 'color': '#9c27b0', 'icon': 'mini-tools'},
    {'filename': 'wall-planter.jpg', 'title': 'Vertical Wall\nPlanter Set', 'color': '#4caf50', 'icon': 'plant'},
    {'filename': 'drip-irrigation.jpg', 'title': 'Drip Irrigation\nKit', 'color': '#03a9f4', 'icon': 'pot'},
    {'filename': 'grow-bags.jpg', 'title': 'Fabric Grow\nBags Set', 'color': '#795548', 'icon': 'soil'},
    {'filename': 'garden-kneeler.jpg', 'title': 'Garden Kneeler\n& Seat', 'color': '#607d8b', 'icon': 'mini-tools'},
    {'filename': 'compost-bin.jpg', 'title': 'Compost Bin\n50L', 'color': '#5d4037', 'icon': 'soil'},
    
    # Growing Kits
    {'filename': 'balcony-farming-kit.jpg', 'title': 'Balcony\nFarming Kit', 'color': '#4a7c59', 'icon': 'plant'},
    {'filename': 'microgreens-kit.jpg', 'title': 'Microgreens\nDIY Kit', 'color': '#6b9b37', 'icon': 'sprout'},
    {'filename': 'herb-garden-kit.jpg', 'title': 'Herb Garden\nKit', 'color': '#4caf50', 'icon': 'leaf'},
    {'filename': 'flower-kit.jpg', 'title': 'Flower\nGardening Kit', 'color': '#e91e63', 'icon': 'flower'},
    {'filename': 'mushroom-kit.jpg', 'title': 'Mushroom\nGrowing Kit', 'color': '#8d6e63', 'icon': 'plant'},
    {'filename': 'succulent-kit.jpg', 'title': 'Cactus &\nSucculent Kit', 'color': '#009688', 'icon': 'pot'},
    {'filename': 'kids-vegetable-kit.jpg', 'title': 'Kids Vegetable\nGrowing Kit', 'color': '#ff9800', 'icon': 'kids'},
    {'filename': 'hydroponic-system.jpg', 'title': 'Hydroponic\nSystem', 'color': '#2196f3', 'icon': 'pot'},
    
    # Soil & Fertilizers
    {'filename': 'potting-mix.jpg', 'title': 'Organic\nPotting Mix', 'color': '#5d4037', 'icon': 'soil'},
    {'filename': 'cocopeat-block.jpg', 'title': 'Cocopeat\nBlock 5kg', 'color': '#8d6e63', 'icon': 'soil'},
    {'filename': 'vermicompost.jpg', 'title': 'Premium\nVermicompost', 'color': '#6d4c41', 'icon': 'soil'},
    {'filename': 'neem-cake.jpg', 'title': 'Neem Cake\nFertilizer', 'color': '#7cb342', 'icon': 'leaf'},
    {'filename': 'flower-potting-mix.jpg', 'title': 'Flower\nPotting Mix', 'color': '#d81b60', 'icon': 'flower'},
    {'filename': 'perlite.jpg', 'title': 'Perlite Soil\nAmendment', 'color': '#eceff1', 'icon': 'soil'},
    {'filename': 'seaweed-fertilizer.jpg', 'title': 'Seaweed\nLiquid', 'color': '#00695c', 'icon': 'leaf'},
    {'filename': 'npk-fertilizer.jpg', 'title': 'Complete NPK\nFertilizer', 'color': '#558b2f', 'icon': 'sprout'},
    
    # Eco-Friendly Gifts
    {'filename': 'rakhi-eco-gift.jpg', 'title': 'Rakhi Eco\nGift Hamper', 'color': '#d84315', 'icon': 'gift'},
    {'filename': 'diwali-gift.jpg', 'title': 'Diwali Green\nGift Box', 'color': '#ff6f00', 'icon': 'gift'},
    {'filename': 'corporate-desk-garden.jpg', 'title': 'Corporate\nDesk Garden', 'color': '#1b5e20', 'icon': 'pot'},
    {'filename': 'birthday-terrarium.jpg', 'title': 'Birthday\nTerrarium Kit', 'color': '#f50057', 'icon': 'gift'},
    {'filename': 'wedding-sapling.jpg', 'title': 'Wedding\nSapling Set', 'color': '#8e24aa', 'icon': 'plant'},
    {'filename': 'mothers-day-rose.jpg', 'title': "Mother's Day\nRose Plant", 'color': '#e91e63', 'icon': 'flower'},
    {'filename': 'valentine-combo.jpg', 'title': 'Valentine\nLove Plant', 'color': '#c51162', 'icon': 'gift'},
    {'filename': 'new-home-set.jpg', 'title': 'New Home\nBlessing Set', 'color': '#00695c', 'icon': 'plant'},
    {'filename': 'corporate-bulk.jpg', 'title': 'Corporate\nBulk Set', 'color': '#37474f', 'icon': 'pot'},
    {'filename': 'christmas-gift.jpg', 'title': 'Christmas\nGreen Hamper', 'color': '#388e3c', 'icon': 'gift'},
    {'filename': 'thank-you-bamboo.jpg', 'title': 'Thank You\nBamboo Set', 'color': '#689f38', 'icon': 'plant'},
    {'filename': 'anniversary-bonsai.jpg', 'title': 'Anniversary\nBonsai Gift', 'color': '#5d4037', 'icon': 'leaf'},
]

print(f"Generating {len(products)} professional product images...\n")

for idx, product in enumerate(products, 1):
    img_path = media_dir / product['filename']
    img = create_product_image(
        product['filename'],
        product['title'],
        product['color'],
        product['icon']
    )
    img.save(img_path, 'JPEG', quality=95, optimize=True)
    print(f"✓ [{idx}/{len(products)}] Created: {product['filename']}")

print(f"\n✅ All {len(products)} product images generated successfully!")
print(f"📁 Images saved to: {media_dir.absolute()}")
print("\n🔄 Run: python update_all_db.py to assign images to products")
