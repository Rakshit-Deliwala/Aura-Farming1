"""
Direct SQLite update script (no Django required)
"""
import sqlite3

# Connect to database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Image mapping
updates = [
    ('products/gardening-toolkit.jpg', 'AURA Premium Gardening Toolkit (8-in-1)'),
    ('products/balcony-farming-kit.jpg', 'Beginner Balcony Farming Kit'),
    ('products/microgreens-kit.jpg', 'Microgreens DIY Kit – 5 Varieties'),
    ('products/potting-mix.jpg', 'Organic Vegetable Potting Mix 10kg'),
    ('products/rakhi-eco-gift.jpg', 'Rakhi Eco-Gift Hamper with Plantable Seeds'),
    ('products/corporate-desk-garden.jpg', 'Corporate Desk Garden Gift Box'),
]

print("Updating product images in database...\n")

updated_count = 0
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

# Commit changes
conn.commit()

# Verify updates
print("\n📋 Current product images:")
cursor.execute("SELECT name, image FROM shop_product")
for row in cursor.fetchall():
    print(f"  - {row[0]}: {row[1] or 'No image'}")

conn.close()

print(f"\n✅ Successfully updated {updated_count} products!")
print("🌐 Refresh your browser at http://127.0.0.1:8000/ to see the images")
