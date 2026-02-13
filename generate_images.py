"""
Standalone script to generate product placeholder images
Run with: python generate_images.py
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
    """Draw custom icon shapes"""
    # Convert color to tuple if it's a string
    if isinstance(color, str):
        color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    # Calculate lighter version for accents
    lighter = tuple(min(255, int(c * 1.3)) for c in color)
    
    if icon_type == 'toolkit':
        # Draw wrench icon
        draw.rectangle([center_x-60, center_y-10, center_x+60, center_y+10], fill=color)
        draw.ellipse([center_x-70, center_y-20, center_x-50, center_y+20], fill=color)
        draw.ellipse([center_x+50, center_y-20, center_x+70, center_y+20], fill=color)
        # Screwdriver
        draw.rectangle([center_x-40, center_y-60, center_x-20, center_y-10], fill=color)
        draw.polygon([center_x-40, center_y-60, center_x-20, center_y-60, center_x-30, center_y-80], fill=color)
        
    elif icon_type == 'plant':
        # Draw plant seedling
        draw.ellipse([center_x-15, center_y+20, center_x+15, center_y+50], fill=color)  # pot
        draw.rectangle([center_x-10, center_y, center_x+10, center_y+20], fill=color)  # stem
        # Leaves
        draw.ellipse([center_x-40, center_y-20, center_x-10, center_y+10], fill=color)
        draw.ellipse([center_x+10, center_y-30, center_x+40, center_y], fill=color)
        draw.ellipse([center_x-25, center_y-40, center_x+5, center_y-10], fill=color)
        
    elif icon_type == 'sprout':
        # Microgreens sprouts
        for i in range(-30, 40, 20):
            draw.rectangle([center_x+i-3, center_y-40, center_x+i+3, center_y+20], fill=color)
            draw.ellipse([center_x+i-8, center_y-50, center_x+i+8, center_y-35], fill=color)
            
    elif icon_type == 'soil':
        # Soil bag shape
        draw.rectangle([center_x-50, center_y-20, center_x+50, center_y+50], fill=color)
        draw.polygon([center_x-50, center_y-20, center_x, center_y-40, center_x+50, center_y-20], fill=color)
        # Dots for soil texture
        for y in range(-10, 40, 15):
            for x in range(-40, 45, 20):
                draw.ellipse([center_x+x-3, center_y+y-3, center_x+x+3, center_y+y+3], fill=lighter)
                
    elif icon_type == 'gift':
        # Gift box
        draw.rectangle([center_x-50, center_y-30, center_x+50, center_y+40], fill=color)
        draw.rectangle([center_x-50, center_y-50, center_x+50, center_y-30], fill=lighter)
        # Ribbon
        draw.rectangle([center_x-5, center_y-50, center_x+5, center_y+40], fill='white')
        draw.rectangle([center_x-50, center_y-5, center_x+50, center_y+5], fill='white')
        # Bow
        draw.ellipse([center_x-20, center_y-70, center_x-5, center_y-50], fill='white')
        draw.ellipse([center_x+5, center_y-70, center_x+20, center_y-50], fill='white')
        
    elif icon_type == 'pot':
        # Potted plant
        draw.polygon([center_x-35, center_y+20, center_x-45, center_y+50, center_x+45, center_y+50, center_x+35, center_y+20], fill=color)
        # Plant in pot
        draw.ellipse([center_x-25, center_y-10, center_x-5, center_y+20], fill='white')
        draw.ellipse([center_x+5, center_y-10, center_x+25, center_y+20], fill='white')
        draw.ellipse([center_x-12, center_y-25, center_x+12, center_y+5], fill='white')


def create_product_image(filename, title, color, icon_type):
    """Create a professional product placeholder image"""
    # Create image with gradient
    img = Image.new('RGB', (800, 800), color=color)
    draw = ImageDraw.Draw(img)
    
    # Create gradient effect
    base_color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    for y in range(800):
        factor = y / 800 * 0.3
        gradient_color = darken_color(color, factor)
        draw.line([(0, y), (800, y)], fill=gradient_color, width=1)
    
    # Add decorative corners
    corner_color = lighten_color(color, 0.2)
    for i in range(0, 100, 10):
        draw.arc([i, i, 200-i, 200-i], 180, 270, fill=corner_color, width=3)
        draw.arc([600+i, i, 800-i, 200-i], 270, 360, fill=corner_color, width=3)
        draw.arc([i, 600+i, 200-i, 800-i], 90, 180, fill=corner_color, width=3)
        draw.arc([600+i, 600+i, 800-i, 800-i], 0, 90, fill=corner_color, width=3)
    
    # Add main border
    border_color = lighten_color(color, 0.4)
    draw.rectangle([30, 30, 770, 770], outline=border_color, width=10)
    
    # Add center white circle
    draw.ellipse([200, 200, 600, 600], fill='white', outline=lighten_color(color, 0.5), width=8)
    
    # Draw icon in center
    icon_color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    draw_icon(draw, icon_type, 400, 400, icon_color)
    
    # Try to use a system font for text, fallback to default
    try:
        # Try Windows fonts
        title_font = ImageFont.truetype("arial.ttf", 48)
        subtitle_font = ImageFont.truetype("arial.ttf", 36)
        brand_font = ImageFont.truetype("arialbd.ttf", 32)
    except:
        try:
            title_font = ImageFont.truetype("Arial.ttf", 48)
            subtitle_font = ImageFont.truetype("Arial.ttf", 36)
            brand_font = ImageFont.truetype("Arial.ttf", 32)
        except:
            # Fallback to default font
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            brand_font = ImageFont.load_default()
    
    # Add product title below circle
    text_y = 640
    for line in title.split('\n'):
        bbox = draw.textbbox((0, 0), line, font=title_font)
        text_width = bbox[2] - bbox[0]
        text_x = (800 - text_width) // 2
        # Add shadow
        draw.text((text_x+2, text_y+2), line, fill=(0, 0, 0, 128), font=title_font)
        draw.text((text_x, text_y), line, fill='white', font=title_font)
        text_y += 55
    
    # Add branding at bottom
    brand_text = "AURA FARMING"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    brand_width = bbox[2] - bbox[0]
    brand_x = (800 - brand_width) // 2
    draw.text((brand_x, 730), brand_text, fill=lighten_color(color, 0.6), font=brand_font)
    
    return img


# Create media/products directory
media_dir = Path('media/products')
media_dir.mkdir(parents=True, exist_ok=True)

# Product configurations
products = [
    {
        'filename': 'gardening-toolkit.jpg',
        'title': 'Premium Gardening\nToolkit 8-in-1',
        'color': '#2d5016',
        'icon': 'toolkit'
    },
    {
        'filename': 'balcony-farming-kit.jpg',
        'title': 'Balcony Farming\nStarter Kit',
        'color': '#4a7c59',
        'icon': 'plant'
    },
    {
        'filename': 'microgreens-kit.jpg',
        'title': 'Microgreens\nDIY Kit',
        'color': '#6b9b37',
        'icon': 'sprout'
    },
    {
        'filename': 'potting-mix.jpg',
        'title': 'Organic Potting\nMix 10kg',
        'color': '#5d4037',
        'icon': 'soil'
    },
    {
        'filename': 'rakhi-eco-gift.jpg',
        'title': 'Rakhi Eco-Gift\nHamper',
        'color': '#d84315',
        'icon': 'gift'
    },
    {
        'filename': 'corporate-desk-garden.jpg',
        'title': 'Corporate Desk\nGarden Box',
        'color': '#1b5e20',
        'icon': 'pot'
    }
]

print("Generating professional product images...\n")

for product in products:
    img_path = media_dir / product['filename']
    img = create_product_image(
        product['filename'],
        product['title'],
        product['color'],
        product['icon']
    )
    img.save(img_path, 'JPEG', quality=95, optimize=True)
    print(f"✓ Created: {img_path}")

print("\n✅ All product images generated successfully!")
print(f"📁 Images saved to: {media_dir.absolute()}")
print("\n🌐 Refresh your browser to see the updated images!")
print("   The server will automatically detect the new files.")

