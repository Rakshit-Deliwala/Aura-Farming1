"""
Fix all product images to match correct image files
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import Product

# Mapping of product names to image filenames
IMAGE_MAPPING = {
    # Toolkits
    'AURA Premium Gardening Toolkit (8-in-1)': 'gardening-toolkit.jpg',
    'AURA Professional Gardening Toolkit (12-in-1)': 'professional-toolkit.jpg',
    'Mini Gardening Tool Set (5-in-1)': 'mini-tool-set.jpg',
    'Balcony Gardening Essentials Kit': 'balcony-essentials.jpg',
    'Bonsai Care Toolkit (7-in-1)': 'bonsai-toolkit.jpg',
    'Kids Gardening Tool Set (6-in-1)': 'kids-tool-set.jpg',
    'Organic Farming Starter Kit': 'organic-farming-kit.jpg',
    'Terrace Gardening Master Kit': 'terrace-master-kit.jpg',
    
    # Individual Tools
    'Japanese Hori Hori Garden Knife': 'hori-knife.jpg',
    'Telescopic Hedge Shears': 'hedge-shears.jpg',
    'Garden Fork - Heavy Duty': 'garden-fork.jpg',
    'Leaf Rake - 22 Tines': 'leaf-rake.jpg',
    'Garden Hoe - Traditional': 'garden-hoe.jpg',
    'Bypass Loppers - 28 inch': 'loppers.jpg',
    'Garden Sprayer - 5 Liter': 'garden-sprayer.jpg',
    'Plant Containers - Terracotta Set of 5': 'terracotta-pots.jpg',
    'Garden Tool Organizer - Wall Mounted': 'tool-organizer.jpg',
    'Greenhouse Mini - Portable': 'mini-greenhouse.jpg',
    'Garden Thermometer & Hygrometer': 'thermometer.jpg',
    'Plant Support Stakes - Bamboo 50 Pack': 'bamboo-stakes.jpg',
    'Garden Knee Pads - Foam Cushion': 'knee-pads.jpg',
    'Rain Gauge - Decorative': 'rain-gauge.jpg',
    'Garden Hose - 30 Meter with Nozzle': 'garden-hose.jpg',
    'Pruning Secateurs - Professional Grade': 'pruning-secateurs.jpg',
    'Stainless Steel Hand Trowel': 'hand-trowel.jpg',
    'Soil pH Tester - 3-in-1': 'soil-tester.jpg',
    'Garden Gloves - Anti-Cut Protection': 'garden-gloves.jpg',
    'Watering Can with Long Spout - 5L': 'watering-can.jpg',
    'Grow Bags Set - 5 Pack (12"×12")': 'grow-bags.jpg',
    'Grow Bags Set - 5 Pack (12"??12")': 'grow-bags.jpg',  # Fallback for encoding issue
    'Compost Bin - 50L Capacity': 'compost-bin.jpg',
    'Drip Irrigation Kit for 25 Plants': 'drip-irrigation.jpg',
    'Vertical Wall Planter Set (6 pockets)': 'wall-planter.jpg',
    'Garden Kneeler & Seat 2-in-1': 'garden-kneeler.jpg',
    
    # Growing Kits
    'Beginner Balcony Farming Kit': 'balcony-farming-kit.jpg',
    'Herb Garden Kit - Kitchen Essentials': 'herb-garden-kit.jpg',
    'Microgreens DIY Kit – 5 Varieties': 'microgreens-kit.jpg',
    'Cactus & Succulent Garden Kit': 'succulent-kit.jpg',
    'Flower Gardening Kit - Seasonal Blooms': 'flower-kit.jpg',
    'Kids Vegetable Growing Kit': 'kids-vegetable-kit.jpg',
    'Mushroom Growing Kit - Oyster Variety': 'mushroom-kit.jpg',
    'Indoor Hydroponic Growing System': 'hydroponic-system.jpg',
    'Tomato Growing Kit - Complete': 'tomato-kit.jpg',
    'Chilli Pepper Growing Kit': 'chilli-kit.jpg',
    'Strawberry Tower Garden Kit': 'strawberry-kit.jpg',
    'Bonsai Starter Kit - Ficus': 'bonsai-starter.jpg',
    'Vertical Garden Wall Kit - 12 Pockets': 'vertical-wall-kit.jpg',
    'Medicinal Herbs Growing Kit': 'medicinal-herbs-kit.jpg',
    'Organic Pest Control Kit': 'pest-control-kit.jpg',
    'Composting Starter Kit': 'compost-starter-kit.jpg',
    'Butterfly & Bee Garden Kit': 'butterfly-garden-kit.jpg',
    'Indoor Air Purifier Plant Kit': 'air-purifier-kit.jpg',
    
    # Soils & Fertilizers
    'Organic Vegetable Potting Mix 10kg': 'potting-mix.jpg',
    'Cocopeat Block - Expands to 5kg': 'cocopeat-block.jpg',
    'Vermicompost - Premium Quality 5kg': 'vermicompost.jpg',
    'Neem Cake Organic Fertilizer 2kg': 'neem-cake.jpg',
    'Complete NPK Fertilizer - Organic 1kg': 'npk-fertilizer.jpg',
    'Perlite - Soil Amendment 1kg': 'perlite.jpg',
    'All-Purpose Flower Potting Mix 5kg': 'flower-potting-mix.jpg',
    'Organic Seaweed Liquid Fertilizer 500ml': 'seaweed-fertilizer.jpg',
    'Cactus & Succulent Special Mix 3kg': 'cactus-mix.jpg',
    'Orchid Potting Mix - Premium 2kg': 'orchid-mix.jpg',
    'Seed Starting Mix - Sterile 5kg': 'seed-starting-mix.jpg',
    'Rose Special Soil Mix 5kg': 'rose-soil.jpg',
    'Activated Charcoal - 500g': 'charcoal.jpg',
    'Vermiculite - Grade 3 (1kg)': 'vermiculite.jpg',
    'Bone Meal Organic Fertilizer 1kg': 'bone-meal.jpg',
    'Cow Manure - Composted 5kg': 'cow-manure.jpg',
    
    # Gifts
    'Rakhi Eco-Gift Hamper with Plantable Seeds': 'rakhi-eco-gift.jpg',
    'Diwali Green Gift Box - Temple Plants': 'diwali-gift.jpg',
    'Christmas Green Gift Hamper': 'christmas-gift.jpg',
    'Corporate Desk Garden Gift Box': 'corporate-desk-garden.jpg',
    'Birthday Terrarium Gift Kit': 'birthday-terrarium.jpg',
    'Anniversary Special - Bonsai Gift': 'anniversary-bonsai.jpg',
    'Mothers Day Special - Rose Plant Gift': 'mothers-day-rose.jpg',
    'Valentine Love Plant Combo': 'valentine-combo.jpg',
    'New Home Blessing Plant Set': 'new-home-set.jpg',
    'Thank You Gift - Bamboo Planter Set': 'thank-you-bamboo.jpg',
    'Wedding Return Gift - Plant Saplings (Set of 25)': 'wedding-sapling.jpg',
    'Corporate Bulk Order - Desk Plants (Set of 50)': 'corporate-bulk.jpg',
    'Teachers Day Plant Gift Set': 'teacher-gift.jpg',
    'Friendship Day Succulent Duo': 'friendship-gift.jpg',
    'Office Desk Mini Garden Set': 'office-mini-garden.jpg',
    'Get Well Soon Plant Gift': 'get-well-gift.jpg',
    'Ganesh Chaturthi Plant Gift': 'ganesh-gift.jpg',
    'Holi Color Garden Kit': 'holi-garden-kit.jpg',
    'Pongal Sugarcane & Plant Gift': 'pongal-gift.jpg',
}

print("=" * 80)
print("Fixing Product Images")
print("=" * 80)
print()

updated = 0
missing = 0
skipped = 0

for product in Product.objects.all():
    if product.name in IMAGE_MAPPING:
        new_image = f"products/{IMAGE_MAPPING[product.name]}"
        old_image = product.image.name if product.image else "None"
        
        if old_image != new_image:
            product.image = new_image
            product.save(update_fields=['image'])
            print(f"✓ Updated: {product.name}")
            print(f"  Old: {old_image}")
            print(f"  New: {new_image}")
            print()
            updated += 1
        else:
            skipped += 1
    else:
        print(f"⚠ Missing mapping: {product.name}")
        missing += 1

print()
print("=" * 80)
print(f"✅ Updated: {updated} products")
print(f"⏭️  Skipped: {skipped} products (already correct)")
print(f"⚠️  Missing: {missing} products (no image mapping)")
print("=" * 80)
