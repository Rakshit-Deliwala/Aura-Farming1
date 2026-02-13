"""
Generate realistic images for 40 new products
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create media/products directory if it doesn't exist
MEDIA_DIR = "media/products"
os.makedirs(MEDIA_DIR, exist_ok=True)

def create_gradient_bg(width, height, color1, color2):
    """Create gradient background"""
    base = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(base)
    for i in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * i / height)
        g = int(color1[1] + (color2[1] - color1[1]) * i / height)
        b = int(color1[2] + (color2[2]) * i / height)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    return base

def draw_tool_knife(draw, cx, cy):
    """Draw Hori knife"""
    # Blade
    draw.polygon([(cx-60, cy-20), (cx+60, cy-10), (cx+60, cy+10), (cx-60, cy+20)], 
                 fill='#C0C0C0', outline='#808080', width=2)
    # Handle
    draw.rectangle([cx-80, cy-15, cx-50, cy+15], fill='#8B4513', outline='#654321', width=2)
    # Details
    for i in range(3):
        draw.line([(cx-75+i*10, cy-15), (cx-75+i*10, cy+15)], fill='#654321', width=1)

def draw_shears(draw, cx, cy):
    """Draw hedge shears"""
    # Blades
    draw.polygon([(cx-50, cy-40), (cx+10, cy-10), (cx-10, cy), (cx-70, cy-30)], 
                 fill='#B0B0B0', outline='#707070', width=2)
    draw.polygon([(cx+50, cy-40), (cx-10, cy-10), (cx+10, cy), (cx+70, cy-30)], 
                 fill='#B0B0B0', outline='#707070', width=2)
    # Handles
    draw.rectangle([cx-60, cy, cx-40, cy+60], fill='#FF6347', outline='#8B0000', width=2)
    draw.rectangle([cx+40, cy, cx+60, cy+60], fill='#FF6347', outline='#8B0000', width=2)

def draw_fork(draw, cx, cy):
    """Draw garden fork"""
    # Tines
    for i in range(4):
        x = cx - 30 + i * 20
        draw.line([(x, cy-50), (x, cy+10)], fill='#C0C0C0', width=5)
    # Base
    draw.rectangle([cx-40, cy+10, cx+40, cy+20], fill='#696969', outline='#404040', width=2)
    # Handle
    draw.rectangle([cx-8, cy+20, cx+8, cy+70], fill='#8B4513', outline='#654321', width=2)

def draw_rake(draw, cx, cy):
    """Draw leaf rake"""
    # Tines (fan shape)
    for i in range(11):
        angle = -60 + i * 12
        x1 = cx + 50 * (i - 5) / 5
        y1 = cy - 20
        x2 = cx + 70 * (i - 5) / 5
        y2 = cy - 40
        draw.line([(x1, y1), (x2, y2)], fill='#FFD700', width=3)
    # Base
    draw.arc([cx-60, cy-30, cx+60, cy-10], 0, 180, fill='#FFD700', width=4)
    # Handle
    draw.rectangle([cx-6, cy-20, cx+6, cy+70], fill='#8B4513', outline='#654321', width=2)

def draw_hoe(draw, cx, cy):
    """Draw garden hoe"""
    # Blade
    draw.rectangle([cx-40, cy-15, cx+40, cy+15], fill='#A9A9A9', outline='#696969', width=2)
    # Neck
    draw.line([(cx, cy+15), (cx, cy+30)], fill='#696969', width=4)
    # Handle
    draw.rectangle([cx-5, cy+30, cx+5, cy+80], fill='#8B4513', outline='#654321', width=2)

def draw_loppers(draw, cx, cy):
    """Draw bypass loppers"""
    # Upper blade
    draw.arc([cx-50, cy-50, cx+50, cy+10], 180, 270, fill='#C0C0C0', width=6)
    # Lower blade
    draw.arc([cx-50, cy-10, cx+50, cy+50], 90, 180, fill='#B0B0B0', width=6)
    # Long handles
    draw.rectangle([cx-60, cy+10, cx-40, cy+90], fill='#FF4500', outline='#8B0000', width=2)
    draw.rectangle([cx+40, cy+10, cx+60, cy+90], fill='#FF4500', outline='#8B0000', width=2)

def draw_sprayer(draw, cx, cy):
    """Draw garden sprayer"""
    # Tank
    draw.ellipse([cx-40, cy-50, cx+40, cy+30], fill='#32CD32', outline='#228B22', width=3)
    # Pump handle
    draw.rectangle([cx-10, cy-70, cx+10, cy-50], fill='#FF6347', outline='#8B0000', width=2)
    # Nozzle wand
    draw.line([(cx+40, cy-20), (cx+80, cy-40)], fill='#696969', width=4)
    # Spray lines
    for i in range(3):
        draw.line([(cx+80, cy-40), (cx+90+i*5, cy-50-i*5)], fill='#87CEEB', width=1)

def draw_terracotta_pots(draw, cx, cy):
    """Draw terracotta pot set"""
    sizes = [(-50, 40), (0, 50), (50, 35)]
    for ox, h in sizes:
        x = cx + ox
        # Pot body
        draw.polygon([(x-25, cy-h), (x-20, cy+20), (x+20, cy+20), (x+25, cy-h)], 
                     fill='#CD853F', outline='#8B4513', width=2)
        # Rim
        draw.ellipse([x-25, cy-h-5, x+25, cy-h+5], fill='#D2691E', outline='#8B4513', width=2)

def draw_organizer(draw, cx, cy):
    """Draw tool organizer"""
    # Board
    draw.rectangle([cx-60, cy-70, cx+60, cy+70], fill='#DEB887', outline='#8B4513', width=3)
    # Hooks
    for i in range(3):
        for j in range(2):
            x = cx - 35 + i * 35
            y = cy - 35 + j * 40
            draw.arc([x-10, y-10, x+10, y+10], 0, 180, fill='#696969', width=4)
    # Tools outline
    draw.line([(cx-40, cy+30), (cx-40, cy+60)], fill='#8B4513', width=3)
    draw.line([(cx, cy+25), (cx, cy+55)], fill='#C0C0C0', width=3)

def draw_greenhouse(draw, cx, cy):
    """Draw mini greenhouse"""
    # Base
    draw.rectangle([cx-60, cy+20, cx+60, cy+70], fill='#90EE90', outline='#228B22', width=2)
    # Roof frame
    draw.polygon([(cx-60, cy+20), (cx, cy-50), (cx+60, cy+20)], 
                 fill='#E0F8E0', outline='#228B22', width=3)
    # Frame lines
    for i in range(5):
        x = cx - 50 + i * 25
        draw.line([(x, cy+20), (x, cy+70)], fill='#228B22', width=2)
    # Door
    draw.rectangle([cx-15, cy+30, cx+15, cy+70], fill='#FFFFFF', outline='#228B22', width=2)

def draw_thermometer(draw, cx, cy):
    """Draw thermometer"""
    # Body
    draw.rectangle([cx-15, cy-60, cx+15, cy+40], fill='#FFFFFF', outline='#000000', width=2)
    # Bulb
    draw.ellipse([cx-20, cy+30, cx+20, cy+70], fill='#FF0000', outline='#8B0000', width=2)
    # Scale
    for i in range(8):
        y = cy - 50 + i * 12
        draw.line([(cx-10, y), (cx-5, y)], fill='#000000', width=1)
    # Mercury
    draw.rectangle([cx-5, cy-30, cx+5, cy+40], fill='#FF0000')

def draw_stakes(draw, cx, cy):
    """Draw bamboo stakes bundle"""
    for i in range(7):
        x = cx - 30 + i * 10
        # Create bamboo texture
        draw.rectangle([x-3, cy-60, x+3, cy+60], fill='#DEB887', outline='#8B4513', width=1)
        # Bamboo segments
        for j in range(6):
            y = cy - 50 + j * 20
            draw.line([(x-3, y), (x+3, y)], fill='#8B4513', width=1)
    # Tie
    draw.rectangle([cx-35, cy-10, cx+35, cy+10], fill='#FF6347')

def draw_knee_pads(draw, cx, cy):
    """Draw knee pads"""
    # Left pad
    draw.ellipse([cx-60, cy-30, cx-10, cy+30], fill='#4169E1', outline='#00008B', width=3)
    draw.ellipse([cx-50, cy-20, cx-20, cy+20], fill='#87CEEB')
    # Right pad
    draw.ellipse([cx+10, cy-30, cx+60, cy+30], fill='#4169E1', outline='#00008B', width=3)
    draw.ellipse([cx+20, cy-20, cx+50, cy+20], fill='#87CEEB')
    # Straps
    draw.rectangle([cx-55, cy-35, cx-15, cy-30], fill='#000000')
    draw.rectangle([cx+15, cy-35, cx+55, cy-30], fill='#000000')

def draw_rain_gauge(draw, cx, cy):
    """Draw rain gauge"""
    # Cylinder
    draw.rectangle([cx-20, cy-60, cx+20, cy+50], fill='#E6F3FF', outline='#4682B4', width=2)
    # Measurements
    for i in range(8):
        y = cy - 50 + i * 14
        draw.line([(cx-20, y), (cx-10, y)], fill='#00008B', width=1)
        draw.line([(cx+10, y), (cx+20, y)], fill='#00008B', width=1)
    # Water
    draw.rectangle([cx-20, cy+20, cx+20, cy+50], fill='#4682B4', outline='#00008B', width=1)
    # Funnel top
    draw.polygon([(cx-30, cy-70), (cx-20, cy-60), (cx+20, cy-60), (cx+30, cy-70)], 
                 fill='#B0C4DE', outline='#4682B4', width=2)

def draw_hose(draw, cx, cy):
    """Draw garden hose"""
    # Coiled hose
    for i in range(4):
        y = cy - 40 + i * 25
        draw.ellipse([cx-50, y-10, cx+50, y+10], fill='#32CD32', outline='#228B22', width=3)
    # Nozzle
    draw.rectangle([cx+50, cy-10, cx+80, cy+10], fill='#FFD700', outline='#DAA520', width=2)
    # Connection
    draw.ellipse([cx-60, cy-5, cx-50, cy+5], fill='#C0C0C0', outline='#808080', width=2)

# Kit drawing functions
def draw_kit_box(draw, cx, cy, color, label_color='#FFFFFF'):
    """Draw a kit box"""
    # Box
    draw.rectangle([cx-70, cy-60, cx+70, cy+60], fill=color, outline='#000000', width=3)
    # Label area
    draw.rectangle([cx-60, cy-50, cx+60, cy-40], fill=label_color, outline='#000000', width=1)
    # Seeds/items
    for i in range(3):
        x = cx - 40 + i * 40
        draw.ellipse([x-15, cy-20, x+15, cy+10], fill='#90EE90', outline='#228B22', width=2)
    # Tools
    draw.line([(cx-30, cy+20), (cx-30, cy+50)], fill='#8B4513', width=3)
    draw.line([(cx+30, cy+20), (cx+30, cy+50)], fill='#C0C0C0', width=3)

def draw_soil_bag(draw, cx, cy, color):
    """Draw soil bag"""
    # Bag body
    draw.rectangle([cx-60, cy-50, cx+60, cy+60], fill=color, outline='#000000', width=2)
    # Top fold
    draw.polygon([(cx-60, cy-50), (cx-50, cy-70), (cx+50, cy-70), (cx+60, cy-50)], 
                 fill=color, outline='#000000', width=2)
    # Texture lines
    for i in range(5):
        y = cy - 30 + i * 20
        draw.line([(cx-55, y), (cx+55, y)], fill='#000000', width=1)
    # Label
    draw.rectangle([cx-40, cy-10, cx+40, cy+20], fill='#FFFFFF', outline='#000000', width=2)

def draw_gift_box_simple(draw, cx, cy, color):
    """Draw gift box"""
    # Box
    draw.rectangle([cx-50, cy-40, cx+50, cy+40], fill=color, outline='#000000', width=2)
    # Ribbon vertical
    draw.rectangle([cx-5, cy-40, cx+5, cy+40], fill='#FFD700')
    # Ribbon horizontal
    draw.rectangle([cx-50, cy-5, cx+50, cy+5], fill='#FFD700')
    # Bow
    draw.ellipse([cx-15, cy-55, cx-5, cy-45], fill='#FFD700', outline='#DAA520', width=1)
    draw.ellipse([cx+5, cy-55, cx+15, cy-45], fill='#FFD700', outline='#DAA520', width=1)
    draw.ellipse([cx-5, cy-50, cx+5, cy-40], fill='#FF6347')

# Product configurations
products = [
    # Tools (15)
    ('hori-knife.jpg', draw_tool_knife, (255, 255, 230), (240, 240, 210), 'Japanese Hori Knife'),
    ('hedge-shears.jpg', draw_shears, (240, 248, 255), (220, 235, 245), 'Hedge Shears'),
    ('garden-fork.jpg', draw_fork, (245, 245, 220), (230, 230, 200), 'Garden Fork'),
    ('leaf-rake.jpg', draw_rake, (255, 250, 240), (240, 235, 225), 'Leaf Rake'),
    ('garden-hoe.jpg', draw_hoe, (245, 255, 250), (225, 240, 235), 'Garden Hoe'),
    ('loppers.jpg', draw_loppers, (255, 245, 238), (240, 230, 220), 'Bypass Loppers'),
    ('garden-sprayer.jpg', draw_sprayer, (240, 255, 240), (220, 240, 220), 'Garden Sprayer'),
    ('terracotta-pots.jpg', draw_terracotta_pots, (255, 250, 240), (240, 235, 225), 'Terracotta Pots'),
    ('tool-organizer.jpg', draw_organizer, (245, 245, 245), (230, 230, 230), 'Tool Organizer'),
    ('mini-greenhouse.jpg', draw_greenhouse, (240, 255, 240), (220, 245, 220), 'Mini Greenhouse'),
    ('thermometer.jpg', draw_thermometer, (248, 248, 255), (235, 235, 245), 'Thermometer'),
    ('bamboo-stakes.jpg', draw_stakes, (255, 250, 240), (240, 235, 225), 'Bamboo Stakes'),
    ('knee-pads.jpg', draw_knee_pads, (240, 248, 255), (225, 235, 245), 'Knee Pads'),
    ('rain-gauge.jpg', draw_rain_gauge, (240, 255, 255), (220, 245, 245), 'Rain Gauge'),
    ('garden-hose.jpg', draw_hose, (245, 255, 245), (230, 245, 230), 'Garden Hose'),
]

# Kits (10) - using kit box
kit_colors = [
    ('tomato-kit.jpg', '#FF6347', 'Tomato Growing Kit'),
    ('chilli-kit.jpg', '#DC143C', 'Chilli Pepper Kit'),
    ('strawberry-kit.jpg', '#FFB6C1', 'Strawberry Tower Kit'),
    ('bonsai-starter.jpg', '#8FBC8F', 'Bonsai Starter Kit'),
    ('vertical-wall-kit.jpg', '#90EE90', 'Vertical Garden Kit'),
    ('medicinal-herbs-kit.jpg', '#9370DB', 'Medicinal Herbs Kit'),
    ('pest-control-kit.jpg', '#7CFC00', 'Pest Control Kit'),
    ('compost-starter-kit.jpg', '#8B4513', 'Composting Starter'),
    ('butterfly-garden-kit.jpg', '#FFD700', 'Butterfly Garden'),
    ('air-purifier-kit.jpg', '#98FB98', 'Air Purifier Kit'),
]

# Soils (8) - using soil bag
soil_colors = [
    ('cactus-mix.jpg', '#F4A460', 'Cactus Mix'),
    ('orchid-mix.jpg', '#DDA0DD', 'Orchid Mix'),
    ('seed-starting-mix.jpg', '#D2B48C', 'Seed Starting Mix'),
    ('rose-soil.jpg', '#FFB6C1', 'Rose Special Soil'),
    ('charcoal.jpg', '#2F4F4F', 'Activated Charcoal'),
    ('vermiculite.jpg', '#F5DEB3', 'Vermiculite'),
    ('bone-meal.jpg', '#F5F5DC', 'Bone Meal'),
    ('cow-manure.jpg', '#8B4513', 'Cow Manure'),
]

# Gifts (7) - using gift box
gift_colors = [
    ('teacher-gift.jpg', '#FF69B4', 'Teachers Day Gift'),
    ('friendship-gift.jpg', '#FFD700', 'Friendship Day Gift'),
    ('office-mini-garden.jpg', '#87CEEB', 'Office Desk Garden'),
    ('get-well-gift.jpg', '#98FB98', 'Get Well Soon Gift'),
    ('ganesh-gift.jpg', '#FFA500', 'Ganesh Chaturthi Gift'),
    ('holi-garden-kit.jpg', '#FF1493', 'Holi Color Garden'),
    ('pongal-gift.jpg', '#FFD700', 'Pongal Sugarcane Gift'),
]

print("Creating 40 realistic product images...")
print()

count = 0

# Create tool images
for filename, draw_func, bg1, bg2, name in products:
    count += 1
    img = create_gradient_bg(800, 800, bg1, bg2)
    draw = ImageDraw.Draw(img)
    
    # Add border
    draw.rectangle([10, 10, 790, 790], outline='#CCCCCC', width=3)
    
    # Draw product
    draw_func(draw, 400, 400)
    
    # Save
    filepath = os.path.join(MEDIA_DIR, filename)
    img.save(filepath, quality=95)
    print(f"✓ [{count}/40] Created: {name}")

# Create kit images
for filename, color, name in kit_colors:
    count += 1
    img = create_gradient_bg(800, 800, (255, 255, 255), (240, 248, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10, 10, 790, 790], outline='#CCCCCC', width=3)
    draw_kit_box(draw, 400, 400, color)
    
    filepath = os.path.join(MEDIA_DIR, filename)
    img.save(filepath, quality=95)
    print(f"✓ [{count}/40] Created: {name}")

# Create soil images
for filename, color, name in soil_colors:
    count += 1
    img = create_gradient_bg(800, 800, (250, 250, 245), (235, 235, 230))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10, 10, 790, 790], outline='#CCCCCC', width=3)
    draw_soil_bag(draw, 400, 400, color)
    
    filepath = os.path.join(MEDIA_DIR, filename)
    img.save(filepath, quality=95)
    print(f"✓ [{count}/40] Created: {name}")

# Create gift images
for filename, color, name in gift_colors:
    count += 1
    img = create_gradient_bg(800, 800, (255, 250, 250), (245, 240, 240))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10, 10, 790, 790], outline='#CCCCCC', width=3)
    draw_gift_box_simple(draw, 400, 400, color)
    
    filepath = os.path.join(MEDIA_DIR, filename)
    img.save(filepath, quality=95)
    print(f"✓ [{count}/40] Created: {name}")

print()
print(f"✅ Created {count} realistic product images!")
print(f"📁 Images saved to: {os.path.abspath(MEDIA_DIR)}")
print("🌐 Refresh browser to see updated images")
