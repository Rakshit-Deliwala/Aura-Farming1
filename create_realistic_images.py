"""
Create realistic product images with actual gardening product illustrations
Run with: python create_realistic_images.py
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math


def create_gradient_bg(width, height, color_start, color_end):
    """Create gradient background"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        ratio = y / height
        r = int(color_start[0] * (1 - ratio) + color_end[0] * ratio)
        g = int(color_start[1] * (1 - ratio) + color_end[1] * ratio)
        b = int(color_start[2] * (1 - ratio) + color_end[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img


def draw_toolkit_illustration(draw, center_x, center_y, scale=1.0):
    """Draw detailed toolkit illustration"""
    # Toolbox
    box_color = (101, 67, 33)  # Brown
    draw.rectangle([
        center_x - 80*scale, center_y - 30*scale,
        center_x + 80*scale, center_y + 40*scale
    ], fill=box_color, outline=(70, 50, 30), width=3)
    
    # Handle
    handle_color = (139, 90, 43)
    draw.arc([center_x - 30*scale, center_y - 50*scale, 
              center_x + 30*scale, center_y - 10*scale], 
             0, 180, fill=handle_color, width=5)
    
    # Tools sticking out
    # Trowel
    draw.polygon([
        (center_x - 50*scale, center_y - 20*scale),
        (center_x - 40*scale, center_y - 60*scale),
        (center_x - 30*scale, center_y - 55*scale),
        (center_x - 35*scale, center_y - 15*scale)
    ], fill=(192, 192, 192))
    
    # Pruner
    draw.ellipse([center_x + 20*scale, center_y - 50*scale, 
                  center_x + 35*scale, center_y - 35*scale], 
                 fill=(200, 50, 50))
    draw.line([center_x + 27*scale, center_y - 50*scale, 
               center_x + 27*scale, center_y - 20*scale], 
              fill=(100, 100, 100), width=3)


def draw_plant_pot(draw, center_x, center_y, scale=1.0):
    """Draw plant in pot"""
    # Pot
    pot_color = (180, 90, 50)
    draw.polygon([
        (center_x - 40*scale, center_y + 10*scale),
        (center_x - 50*scale, center_y + 50*scale),
        (center_x + 50*scale, center_y + 50*scale),
        (center_x + 40*scale, center_y + 10*scale)
    ], fill=pot_color, outline=(120, 60, 30), width=2)
    
    # Soil
    draw.ellipse([center_x - 40*scale, center_y, 
                  center_x + 40*scale, center_y + 20*scale], 
                 fill=(101, 67, 33))
    
    # Plant leaves
    leaf_color = (34, 139, 34)
    for i, angle in enumerate([0, 60, 120, 180, 240, 300]):
        rad = math.radians(angle)
        x = center_x + 25*scale * math.cos(rad)
        y = center_y - 20*scale + 25*scale * math.sin(rad)
        draw.ellipse([x - 15*scale, y - 10*scale, 
                      x + 15*scale, y + 10*scale], 
                     fill=leaf_color, outline=(20, 100, 20), width=1)
    
    # Center
    draw.ellipse([center_x - 15*scale, center_y - 30*scale, 
                  center_x + 15*scale, center_y], 
                 fill=(50, 150, 50))


def draw_seeds(draw, center_x, center_y, scale=1.0):
    """Draw seed packet"""
    # Packet
    draw.rectangle([
        center_x - 50*scale, center_y - 60*scale,
        center_x + 50*scale, center_y + 40*scale
    ], fill=(255, 255, 240), outline=(100, 100, 100), width=2)
    
    # Seeds illustration
    for i in range(5):
        for j in range(4):
            x = center_x - 30*scale + i * 15*scale
            y = center_y - 30*scale + j * 15*scale
            draw.ellipse([x - 4*scale, y - 3*scale, 
                          x + 4*scale, y + 3*scale], 
                         fill=(139, 69, 19))


def draw_soil_bag(draw, center_x, center_y, scale=1.0):
    """Draw soil bag"""
    # Bag body
    bag_color = (139, 90, 43)
    draw.rectangle([
        center_x - 60*scale, center_y - 20*scale,
        center_x + 60*scale, center_y + 50*scale
    ], fill=bag_color, outline=(90, 60, 30), width=2)
    
    # Top fold
    draw.polygon([
        (center_x - 60*scale, center_y - 20*scale),
        (center_x - 40*scale, center_y - 40*scale),
        (center_x + 40*scale, center_y - 40*scale),
        (center_x + 60*scale, center_y - 20*scale)
    ], fill=(160, 110, 60), outline=(90, 60, 30), width=2)
    
    # Soil texture
    for i in range(15):
        x = center_x - 50*scale + (i % 5) * 25*scale
        y = center_y - 10*scale + (i // 5) * 20*scale
        draw.ellipse([x - 3*scale, y - 3*scale, 
                      x + 3*scale, y + 3*scale], 
                     fill=(101, 67, 33))


def draw_gift_box(draw, center_x, center_y, scale=1.0):
    """Draw gift box with bow"""
    # Box
    box_color = (220, 20, 60)
    draw.rectangle([
        center_x - 60*scale, center_y - 30*scale,
        center_x + 60*scale, center_y + 50*scale
    ], fill=box_color, outline=(150, 10, 40), width=2)
    
    # Ribbon vertical
    draw.rectangle([
        center_x - 8*scale, center_y - 30*scale,
        center_x + 8*scale, center_y + 50*scale
    ], fill=(255, 215, 0))
    
    # Ribbon horizontal
    draw.rectangle([
        center_x - 60*scale, center_y + 2*scale,
        center_x + 60*scale, center_y + 18*scale
    ], fill=(255, 215, 0))
    
    # Bow
    draw.ellipse([center_x - 30*scale, center_y - 60*scale, 
                  center_x - 10*scale, center_y - 35*scale], 
                 fill=(255, 215, 0), outline=(200, 170, 0), width=2)
    draw.ellipse([center_x + 10*scale, center_y - 60*scale, 
                  center_x + 30*scale, center_y - 35*scale], 
                 fill=(255, 215, 0), outline=(200, 170, 0), width=2)
    draw.ellipse([center_x - 12*scale, center_y - 50*scale, 
                  center_x + 12*scale, center_y - 30*scale], 
                 fill=(255, 215, 0))


def draw_watering_can(draw, center_x, center_y, scale=1.0):
    """Draw watering can"""
    # Can body
    can_color = (70, 130, 180)
    draw.ellipse([center_x - 40*scale, center_y - 20*scale, 
                  center_x + 40*scale, center_y + 40*scale], 
                 fill=can_color, outline=(50, 100, 150), width=2)
    
    # Spout
    draw.polygon([
        (center_x + 35*scale, center_y),
        (center_x + 60*scale, center_y - 25*scale),
        (center_x + 65*scale, center_y - 20*scale),
        (center_x + 40*scale, center_y + 5*scale)
    ], fill=can_color, outline=(50, 100, 150), width=1)
    
    # Handle
    draw.arc([center_x - 50*scale, center_y - 30*scale, 
              center_x + 10*scale, center_y + 10*scale], 
             90, 270, fill=(50, 100, 150), width=4)


def draw_flower(draw, center_x, center_y, scale=1.0):
    """Draw flower"""
    # Petals
    petal_color = (255, 105, 180)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        x = center_x + 30*scale * math.cos(rad)
        y = center_y + 30*scale * math.sin(rad)
        draw.ellipse([x - 15*scale, y - 20*scale, 
                      x + 15*scale, y + 20*scale], 
                     fill=petal_color, outline=(200, 50, 100), width=1)
    
    # Center
    draw.ellipse([center_x - 15*scale, center_y - 15*scale, 
                  center_x + 15*scale, center_y + 15*scale], 
                 fill=(255, 215, 0), outline=(200, 170, 0), width=2)


def create_product_image(filename, title, bg_color_start, bg_color_end, illustration_type):
    """Create realistic product image"""
    width, height = 800, 800
    
    # Create background
    img = create_gradient_bg(width, height, bg_color_start, bg_color_end)
    draw = ImageDraw.Draw(img)
    
    # Add decorative border
    border_color = tuple(min(255, c + 30) for c in bg_color_end)
    for i in range(5):
        draw.rectangle([10+i, 10+i, width-10-i, height-10-i], 
                      outline=border_color, width=1)
    
    # White circle background for illustration
    draw.ellipse([200, 200, 600, 600], 
                fill=(255, 255, 255), 
                outline=border_color, width=8)
    
    # Draw illustration
    center_x, center_y = 400, 400
    
    if illustration_type == 'toolkit':
        draw_toolkit_illustration(draw, center_x, center_y, 1.5)
    elif illustration_type == 'plant':
        draw_plant_pot(draw, center_x, center_y, 1.8)
    elif illustration_type == 'seeds':
        draw_seeds(draw, center_x, center_y, 1.5)
    elif illustration_type == 'soil':
        draw_soil_bag(draw, center_x, center_y, 1.5)
    elif illustration_type == 'gift':
        draw_gift_box(draw, center_x, center_y, 1.3)
    elif illustration_type == 'watering':
        draw_watering_can(draw, center_x, center_y, 1.5)
    elif illustration_type == 'flower':
        draw_flower(draw, center_x, center_y, 1.5)
    
    # Add text
    try:
        title_font = ImageFont.truetype("arial.ttf", 52)
        brand_font = ImageFont.truetype("arialbd.ttf", 36)
    except:
        title_font = ImageFont.load_default()
        brand_font = ImageFont.load_default()
    
    # Product title
    text_y = 640
    for line in title.split('\\n'):
        bbox = draw.textbbox((0, 0), line, font=title_font)
        text_width = bbox[2] - bbox[0]
        text_x = (width - text_width) // 2
        # Shadow
        draw.text((text_x + 3, text_y + 3), line, fill=(0, 0, 0, 80), font=title_font)
        # Main text
        draw.text((text_x, text_y), line, fill=(255, 255, 255), font=title_font)
        text_y += 60
    
    # Brand
    brand_text = "AURA FARMING"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    brand_width = bbox[2] - bbox[0]
    brand_x = (width - brand_width) // 2
    brand_color = tuple(min(255, c + 80) for c in bg_color_end)
    draw.text((brand_x, 730), brand_text, fill=brand_color, font=brand_font)
    
    return img


# Main execution
media_dir = Path('media/products')
media_dir.mkdir(parents=True, exist_ok=True)

# Select products for realistic illustrations
products = [
    # Top priority products with realistic illustrations
    {'filename': 'gardening-toolkit.jpg', 'title': 'Premium Gardening\\nToolkit 8-in-1', 
     'bg_start': (40, 80, 20), 'bg_end': (60, 120, 40), 'type': 'toolkit'},
    
    {'filename': 'mini-tool-set.jpg', 'title': 'Mini Tool Set\\n5-in-1', 
     'bg_start': (50, 100, 60), 'bg_end': (70, 140, 80), 'type': 'toolkit'},
    
    {'filename': 'balcony-farming-kit.jpg', 'title': 'Balcony Farming\\nStarter Kit',
     'bg_start': (50, 100, 60), 'bg_end': (70, 140, 80), 'type': 'plant'},
    
    {'filename': 'microgreens-kit.jpg', 'title': 'Microgreens\\nDIY Kit',
     'bg_start': (80, 140, 50), 'bg_end': (100, 170, 70), 'type': 'seeds'},
    
    {'filename': 'potting-mix.jpg', 'title': 'Organic Potting\\nMix 10kg',
     'bg_start': (80, 60, 40), 'bg_end': (110, 80, 50), 'type': 'soil'},
    
    {'filename': 'rakhi-eco-gift.jpg', 'title': 'Rakhi Eco\\nGift Hamper',
     'bg_start': (200, 60, 20), 'bg_end': (220, 80, 40), 'type': 'gift'},
    
    {'filename': 'watering-can.jpg', 'title': 'Watering Can\\n5L Capacity',
     'bg_start': (30, 100, 150), 'bg_end': (50, 130, 180), 'type': 'watering'},
    
    {'filename': 'flower-kit.jpg', 'title': 'Flower Gardening\\nKit',
     'bg_start': (200, 30, 100), 'bg_end': (230, 60, 140), 'type': 'flower'},
    
    {'filename': 'herb-garden-kit.jpg', 'title': 'Herb Garden\\nKit',
     'bg_start': (60, 150, 60), 'bg_end': (80, 180, 80), 'type': 'plant'},
    
    {'filename': 'corporate-desk-garden.jpg', 'title': 'Corporate Desk\\nGarden',
     'bg_start': (20, 80, 30), 'bg_end': (40, 110, 50), 'type': 'plant'},
]

print(f"Creating {len(products)} realistic product images...\\n")

for idx, product in enumerate(products, 1):
    img_path = media_dir / product['filename']
    img = create_product_image(
        product['filename'],
        product['title'],
        product['bg_start'],
        product['bg_end'],
        product['type']
    )
    img.save(img_path, 'JPEG', quality=95, optimize=True)
    print(f"✓ [{idx}/{len(products)}] Created: {product['filename']}")

print(f"\\n✅ Created {len(products)} realistic product images!")
print(f"📁 Images saved to: {media_dir.absolute()}")
print("🌐 Refresh browser to see updated images")
