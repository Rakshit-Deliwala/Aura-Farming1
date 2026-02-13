"""
Update database with all product images
Run with: python update_all_db.py
"""
import sqlite3

# Connect to database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Image mapping for all products
updates = [
    # Toolkits
    ('products/gardening-toolkit.jpg', 'AURA Premium Gardening Toolkit (8-in-1)'),
    ('products/mini-tool-set.jpg', 'Mini Gardening Tool Set (5-in-1)'),
    ('products/professional-toolkit.jpg', 'AURA Professional Gardening Toolkit (12-in-1)'),
    ('products/kids-tool-set.jpg', 'Kids Gardening Tool Set (6-in-1)'),
    ('products/balcony-essentials.jpg', 'Balcony Gardening Essentials Kit'),
    ('products/terrace-master-kit.jpg', 'Terrace Gardening Master Kit'),
    ('products/bonsai-toolkit.jpg', 'Bonsai Care Toolkit (7-in-1)'),
    ('products/organic-farming-kit.jpg', 'Organic Farming Starter Kit'),
    
    # Individual Tools
    ('products/hand-trowel.jpg', 'Stainless Steel Hand Trowel'),
    ('products/pruning-secateurs.jpg', 'Pruning Secateurs  - Professional Grade'),
    ('products/garden-gloves.jpg', 'Garden Gloves - Anti-Cut Protection'),
    ('products/watering-can.jpg', 'Watering Can with Long Spout - 5L'),
    ('products/soil-tester.jpg', 'Soil pH Tester - 3-in-1'),
    ('products/wall-planter.jpg', 'Vertical Wall Planter Set (6 pockets)'),
    ('products/drip-irrigation.jpg', 'Drip Irrigation Kit for 25 Plants'),
    ('products/grow-bags.jpg', 'Grow Bags Set - 5 Pack (12"×12")'),
    ('products/garden-kneeler.jpg', 'Garden Kneeler & Seat 2-in-1'),
    ('products/compost-bin.jpg', 'Compost Bin - 50L Capacity'),
    
    # Growing Kits
    ('products/balcony-farming-kit.jpg', 'Beginner Balcony Farming Kit'),
    ('products/microgreens-kit.jpg', 'Microgreens DIY Kit – 5 Varieties'),
    ('products/herb-garden-kit.jpg', 'Herb Garden Kit - Kitchen Essentials'),
    ('products/flower-kit.jpg', 'Flower Gardening Kit - Seasonal Blooms'),
    ('products/mushroom-kit.jpg', 'Mushroom Growing Kit - Oyster Variety'),
    ('products/succulent-kit.jpg', 'Cactus & Succulent Garden Kit'),
    ('products/kids-vegetable-kit.jpg', 'Kids Vegetable Growing Kit'),
    ('products/hydroponic-system.jpg', 'Indoor Hydroponic Growing System'),
    
    # Soil & Fertilizers
    ('products/potting-mix.jpg', 'Organic Vegetable Potting Mix 10kg'),
    ('products/cocopeat-block.jpg', 'Cocopeat Block - Expands to 5kg'),
    ('products/vermicompost.jpg', 'Vermicompost - Premium Quality 5kg'),
    ('products/neem-cake.jpg', 'Neem Cake Organic Fertilizer 2kg'),
    ('products/flower-potting-mix.jpg', 'All-Purpose Flower Potting Mix 5kg'),
    ('products/perlite.jpg', 'Perlite - Soil Amendment 1kg'),
    ('products/seaweed-fertilizer.jpg', 'Organic Seaweed Liquid Fertilizer 500ml'),
    ('products/npk-fertilizer.jpg', 'Complete NPK Fertilizer - Organic 1kg'),
    
    # Eco-Friendly Gifts
    ('products/rakhi-eco-gift.jpg', 'Rakhi Eco-Gift Hamper with Plantable Seeds'),
    ('products/diwali-gift.jpg', 'Diwali Green Gift Box - Temple Plants'),
    ('products/corporate-desk-garden.jpg', 'Corporate Desk Garden Gift Box'),
    ('products/birthday-terrarium.jpg', 'Birthday Terrarium Gift Kit'),
    ('products/wedding-sapling.jpg', 'Wedding Return Gift - Plant Saplings (Set of 25)'),
    ('products/mothers-day-rose.jpg', 'Mothers Day Special - Rose Plant Gift'),
    ('products/valentine-combo.jpg', 'Valentine Love Plant Combo'),
    ('products/new-home-set.jpg', 'New Home Blessing Plant Set'),
    ('products/corporate-bulk.jpg', 'Corporate Bulk Order - Desk Plants (Set of 50)'),
    ('products/christmas-gift.jpg', 'Christmas Green Gift Hamper'),
    ('products/thank-you-bamboo.jpg', 'Thank You Gift - Bamboo Planter Set'),
    ('products/anniversary-bonsai.jpg', 'Anniversary Special - Bonsai Gift'),
]

print("Updating product images in database...\n")

updated_count = 0
not_found = []

for image_path, product_name in updates:
    cursor.execute(
        "UPDATE shop_product SET image = ? WHERE name = ?",
        (image_path, product_name)
    )
    if cursor.rowcount > 0:
        print(f"✓ Updated: {product_name}")
        updated_count += 1
    else:
        print(f"✗ Not found: {product_name}")
        not_found.append(product_name)

# Commit changes
conn.commit()

# Verify updates
print(f"\n📊 Summary:")
print(f"   ✓ Updated: {updated_count} products")
print(f"   ✗ Not found: {len(not_found)} products")

if not_found:
    print(f"\n⚠️  Products not found in database:")
    for name in not_found:
        print(f"   - {name}")

conn.close()

print(f"\n✅ Database update complete!")
print("🌐 Refresh your browser to see all product images")
