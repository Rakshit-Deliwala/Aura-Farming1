"""
Apply database migrations for service request updates
"""
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

print("Adding new fields to ServiceRequest table...")

# Add new columns
try:
    cursor.execute("ALTER TABLE shop_servicerequest ADD COLUMN budget VARCHAR(20) DEFAULT ''")
    print("✓ Added budget column")
except sqlite3.OperationalError:
    print("⚠ budget column already exists")

try:
    cursor.execute("ALTER TABLE shop_servicerequest ADD COLUMN area_size VARCHAR(20) DEFAULT ''")
    print("✓ Added area_size column")
except sqlite3.OperationalError:
    print("⚠ area_size column already exists")

try:
    cursor.execute("ALTER TABLE shop_servicerequest ADD COLUMN preferred_date DATE")
    print("✓ Added preferred_date column")
except sqlite3.OperationalError:
    print("⚠ preferred_date column already exists")

try:
    cursor.execute("ALTER TABLE shop_servicerequest ADD COLUMN address TEXT DEFAULT ''")
    print("✓ Added address column")
except sqlite3.OperationalError:
    print("⚠ address column already exists")

conn.commit()
conn.close()

print("\n✅ Database schema updated successfully!")
print("🌐 Service request form is now enhanced with budget, area, date & address fields")
