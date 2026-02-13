import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import Product

# Mapping of product names to Unsplash image URLs
# These are high-quality, free-to-use images from Unsplash
product_images = {
    # Gardening Toolkits
    'AURA Premium Gardening Toolkit (8-in-1)': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=800&q=80',  # Garden tools set
    'Mini Gardening Tool Set (5-in-1)': 'https://images.unsplash.com/photo-1617576683096-00fc8eecb3af?w=800&q=80',  # Mini gardening tools
    'AURA Professional Gardening Toolkit (12-in-1)': 'https://images.unsplash.com/photo-1589923188900-85dae523342b?w=800&q=80',  # Professional garden tools
    'Kids Gardening Tool Set (6-in-1)': 'https://images.unsplash.com/photo-1601313017745-e197bc5925b5?w=800&q=80',  # Kids gardening
    'Balcony Gardening Essentials Kit': 'https://images.unsplash.com/photo-1509423350716-97f9360b4e09?w=800&q=80',  # Balcony garden
    'Terrace Gardening Master Kit': 'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=800&q=80',  # Terrace garden
    'Bonsai Care Toolkit (7-in-1)': 'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=800&q=80',  # Bonsai tools
    'Organic Farming Starter Kit': 'https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=800&q=80',  # Organic farming
    
    # Individual Tools
    'Stainless Steel Hand Trowel': 'https://images.unsplash.com/photo-1617576683096-00fc8eecb3af?w=800&q=80',  # Hand trowel
    'Pruning Secateurs - Professional Grade': 'https://images.unsplash.com/photo-1617127365659-c47fa864d8bc?w=800&q=80',  # Pruning shears
    'Garden Gloves - Anti-Cut Protection': 'https://images.unsplash.com/photo-1513883049090-d0b7439799bf?w=800&q=80',  # Garden gloves
    'Watering Can with Long Spout - 5L': 'https://images.unsplash.com/photo-1455659817273-f96807779a8a?w=800&q=80',  # Watering can
    'Soil pH Tester - 3-in-1': 'https://images.unsplash.com/photo-1622383563227-04401ab4e5ea?w=800&q=80',  # Soil tester
    'Vertical Wall Planter Set (6 pockets)': 'https://images.unsplash.com/photo-1585494156145-1c60a4fe952b?w=800&q=80',  # Wall planter
    'Drip Irrigation Kit for 25 Plants': 'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=800&q=80',  # Drip irrigation
    'Grow Bags Set - 5 Pack (12"×12")': 'https://images.unsplash.com/photo-1584479898061-15742659937f?w=800&q=80',  # Grow bags
    'Garden Kneeler & Seat 2-in-1': 'https://images.unsplash.com/photo-1621452773781-0f992fd1f5cb?w=800&q=80',  # Garden kneeler
    'Compost Bin - 50L Capacity': 'https://images.unsplash.com/photo-1621452773781-0f992fd1f5cb?w=800&q=80',  # Compost bin
    
    # DIY Growing Kits
    'Beginner Balcony Farming Kit': 'https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?w=800&q=80',  # Balcony farming kit
    'Microgreens DIY Kit – 5 Varieties': 'https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=800&q=80',  # Microgreens
    'Herb Garden Kit - Kitchen Essentials': 'https://images.unsplash.com/photo-1509587584298-0f3b3a3a1797?w=800&q=80',  # Herb garden kit
    'Flower Gardening Kit - Seasonal Blooms': 'https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=800&q=80',  # Flower seeds
    'Mushroom Growing Kit - Oyster Variety': 'https://images.unsplash.com/photo-1617565924217-c7d38173e30c?w=800&q=80',  # Mushrooms
    'Cactus & Succulent Garden Kit': 'https://images.unsplash.com/photo-1509423350716-97f9360b4e09?w=800&q=80',  # Succulents
    'Vegetable Seed Kit - Indian Seasonal Mix': 'https://images.unsplash.com/photo-1591035897819-f4bdf739f446?w=800&q=80',  # Vegetable seeds
    'Bonsai Starter Kit - Ficus Variety': 'https://images.unsplash.com/photo-1588365076098-26229b201aa1?w=800&q=80',  # Bonsai plant
    
    # Soil & Fertilizers
    'Vermicompost (5kg) - Premium Earthworm Casting': 'https://images.unsplash.com/photo-1589923188900-85dae523342b?w=800&q=80',  # Compost
    'Organic Potting Mix (10kg) - Ready to Use': 'https://images.unsplash.com/photo-1592419044706-39796d40f98c?w=800&q=80',  # Potting soil
    'Cocopeat Block - 5kg (Expands to 75L)': 'https://images.unsplash.com/photo-1628697459268-4f69f4a4af24?w=800&q=80',  # Cocopeat
    'Neem Oil - Organic Pest Control (500ml)': 'https://images.unsplash.com/photo-1588365076098-26229b201aa1?w=800&q=80',  # Neem oil bottle
    'Bone Meal Fertilizer - 2kg': 'https://images.unsplash.com/photo-1611518041398-96c724a7cd13?w=800&q=80',  # Fertilizer
    'Perlite for Soil Aeration - 5L': 'https://images.unsplash.com/photo-1625246296958-c2c4f2a7364f?w=800&q=80',  # Perlite
    'Mustard Cake Fertilizer - Organic 2kg': 'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=800&q=80',  # Organic fertilizer
    'Garden Lime - pH Adjuster 1kg': 'https://images.unsplash.com/photo-1617576683096-00fc8eecb3af?w=800&q=80',  # Garden lime
    
    # Eco-Friendly Gifts
    'Plantable Seed Paper Rakhi': 'https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=800&q=80',  # Rakhi with plants
    'Eco Desk Garden Box': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=800&q=80',  # Desk garden
    'Terrarium DIY Kit - Glass Globe': 'https://images.unsplash.com/photo-1527359443443-8a52daed1cbf?w=800&q=80',  # Terrarium
    'Seed Bomb Gift Set - Wildflowers': 'https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=800&q=80',  # Seed bombs
    'Lucky Bamboo Plant Set': 'https://images.unsplash.com/photo-1604762512029-1e6bcadc0bcc?w=800&q=80',  # Bamboo plant
    'Air Purifying Plant Combo (3 plants)': 'https://images.unsplash.com/photo-1463936575829-25148e1db1b8?w=800&q=80',  # Indoor plants
    'Miniature Zen Garden Kit': 'https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?w=800&q=80',  # Zen garden
    'Growing Kit - Thank You Gift': 'https://images.unsplash.com/photo-1558904541-efa843a96f01?w=800&q=80',  # Gift box
    'Corporate Gift Hamper - Green Office': 'https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=800&q=80',  # Corporate gift
    'Festive Plant Gift Box - Diwali Special': 'https://images.unsplash.com/photo-1540479859555-17af45c78602?w=800&q=80',  # Festival gift
}

def update_product_images():
    """Update all products with Unsplash image URLs"""
    updated_count = 0
    not_found = []
    
    for product_name, image_url in product_images.items():
        try:
            product = Product.objects.get(name=product_name)
            # Store the URL in the image_url field
            product.image_url = image_url
            product.save()
            updated_count += 1
            print(f"✓ Updated: {product_name}")
        except Product.DoesNotExist:
            not_found.append(product_name)
            print(f"✗ Not found: {product_name}")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Updated: {updated_count}")
    print(f"  Not found: {len(not_found)}")
    
    if not_found:
        print(f"\nMissing products:")
        for name in not_found:
            print(f"  - {name}")

if __name__ == '__main__':
    print("Starting product image update...\n")
    update_product_images()
    print("\nDone!")
