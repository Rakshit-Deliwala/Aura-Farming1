"""
Add comprehensive gardening tools, kits, products and accessories
Run with: Get-Content add_more_products.py | python manage.py shell
"""
from shop.models import Category, Product

# Get categories
categories = {cat.slug: cat for cat in Category.objects.all()}
tools = categories.get('tools-accessories')
kits = categories.get('diy-kits')
soil = categories.get('fertilizers-soils')
gifts = categories.get('eco-gifts')

print(f"Current products: {Product.objects.count()}")

# New comprehensive products
new_products = [
    # ADVANCED GARDENING TOOLS (15 items)
    Product(name='Japanese Hori Hori Garden Knife', category=tools, category_type='tools', price_inr=1299, stock=45,
            description='Multi-purpose Japanese digging knife with serrated edge, depth markers, and leather sheath. Perfect for weeding, transplanting, and root cutting.',
            tags='tools, knife, japanese, professional', image='products/hori-knife.jpg'),
    
    Product(name='Telescopic Hedge Shears', category=tools, category_type='tools', price_inr=1799, stock=35,
            description='Extendable hedge trimmer with anti-slip handles. Adjustable length 60-90cm. Sharp wavy blades for clean cuts.',
            tags='tools, shears, hedge, trimming', image='products/hedge-shears.jpg'),
    
    Product(name='Garden Fork - Heavy Duty', category=tools, category_type='tools', price_inr=899, stock=55,
            description='Forged steel 4-prong garden fork with D-grip handle. Ideal for turning soil, composting, and breaking up hard ground.',
            tags='tools, fork, digging, heavy-duty', image='products/garden-fork.jpg'),
    
    Product(name='Leaf Rake - 22 Tines', category=tools, category_type='tools', price_inr=649, stock=60,
            description='Lightweight 22-tine leaf rake with adjustable width. Perfect for gathering leaves and garden debris.',
            tags='tools, rake, leaves, cleanup', image='products/leaf-rake.jpg'),
    
    Product(name='Garden Hoe - Traditional', category=tools, category_type='tools', price_inr=549, stock=70,
            description='Traditional hoe with sharp blade for weeding and cultivating. Wooden handle for comfortable grip.',
            tags='tools, hoe, weeding, traditional', image='products/garden-hoe.jpg'),
    
    Product(name='Bypass Loppers - 28 inch', category=tools, category_type='tools', price_inr=1499, stock=40,
            description='Professional bypass loppers with telescopic handles. Cut branches up to 2 inches thick with ease.',
            tags='tools, loppers, pruning, professional', image='products/loppers.jpg'),
    
    Product(name='Garden Sprayer - 5 Liter', category=tools, category_type='tools', price_inr=899, stock=50,
            description='Pressure sprayer with adjustable nozzle. Perfect for pesticides, fertilizers, and water spraying.',
            tags='tools, sprayer, pressure, pesticide', image='products/garden-sprayer.jpg'),
    
    Product(name='Plant Containers - Terracotta Set of 5', category=tools, category_type='tools', price_inr=1299, stock=45,
            description='Authentic terracotta pots set (6", 8", 10", 12", 14") with drainage holes. Classic design for indoor and outdoor plants.',
            tags='tools, pots, terracotta, containers', image='products/terracotta-pots.jpg'),
    
    Product(name='Garden Tool Organizer - Wall Mounted', category=tools, category_type='tools', price_inr=1199, stock=30,
            description='Heavy-duty wall-mounted tool rack with 12 hooks and shelf. Organize all your gardening tools efficiently.',
            tags='tools, organizer, storage, wall-mount', image='products/tool-organizer.jpg'),
    
    Product(name='Greenhouse Mini - Portable', category=tools, category_type='tools', price_inr=3999, stock=20,
            description='Portable mini greenhouse (120x60x80cm) with clear PVC cover and steel frame. Perfect for seedlings and small plants.',
            tags='tools, greenhouse, portable, seedlings', image='products/mini-greenhouse.jpg'),
    
    Product(name='Garden Thermometer & Hygrometer', category=tools, category_type='tools', price_inr=699, stock=55,
            description='Digital outdoor thermometer and humidity gauge. Monitor temperature and moisture levels for optimal plant growth.',
            tags='tools, thermometer, hygrometer, digital', image='products/thermometer.jpg'),
    
    Product(name='Plant Support Stakes - Bamboo 50 Pack', category=tools, category_type='tools', price_inr=449, stock=80,
            description='Natural bamboo stakes (60cm) for supporting plants, vegetables, and flowers. Eco-friendly and durable.',
            tags='tools, stakes, bamboo, support', image='products/bamboo-stakes.jpg'),
    
    Product(name='Garden Knee Pads - Foam Cushion', category=tools, category_type='tools', price_inr=599, stock=65,
            description='Comfortable foam knee pads with adjustable straps. Protect knees while gardening for extended periods.',
            tags='tools, knee-pads, comfort, protection', image='products/knee-pads.jpg'),
    
    Product(name='Rain Gauge - Decorative', category=tools, category_type='tools', price_inr=499, stock=50,
            description='Decorative rain gauge with clear measuring tube. Track rainfall to optimize watering schedule.',
            tags='tools, rain-gauge, measurement, decorative', image='products/rain-gauge.jpg'),
    
    Product(name='Garden Hose - 30 Meter with Nozzle', category=tools, category_type='tools', price_inr=2499, stock=35,
            description='Heavy-duty 30m expandable garden hose with 7-pattern spray nozzle. Lightweight and kink-resistant.',
            tags='tools, hose, watering, expandable', image='products/garden-hose.jpg'),
    
    # SPECIALIZED GROWING KITS (10 items)
    Product(name='Tomato Growing Kit - Complete', category=kits, category_type='kits', price_inr=1899, stock=40,
            description='Complete tomato growing setup with hybrid seeds (cherry, beefsteak), grow bags, stakes, clips, and feeding guide.',
            tags='kits, tomato, vegetables, complete', image='products/tomato-kit.jpg', is_kit=True),
    
    Product(name='Chilli Pepper Growing Kit', category=kits, category_type='kits', price_inr=1599, stock=45,
            description='Grow your own chilies! Includes 4 varieties (green chilli, red chilli, bhut jolokia, capsicum), pots, and care guide.',
            tags='kits, chilli, spices, hot', image='products/chilli-kit.jpg', is_kit=True),
    
    Product(name='Strawberry Tower Garden Kit', category=kits, category_type='kits', price_inr=2499, stock=30,
            description='Vertical strawberry planter with 5 tiers. Includes strawberry plants, soil mix, and feeding instructions.',
            tags='kits, strawberry, fruits, vertical', image='products/strawberry-kit.jpg', is_kit=True),
    
    Product(name='Bonsai Starter Kit - Ficus', category=kits, category_type='kits', price_inr=2199, stock=25,
            description='Begin your bonsai journey with ficus plant, training wire, specialized tools, pot, and comprehensive guide.',
            tags='kits, bonsai, ficus, starter', image='products/bonsai-starter.jpg', is_kit=True),
    
    Product(name='Vertical Garden Wall Kit - 12 Pockets', category=kits, category_type='kits', price_inr=2899, stock=35,
            description='Create living wall art! 12-pocket vertical planter with drip irrigation, soil mix, and plant selection guide.',
            tags='kits, vertical, wall, space-saving', image='products/vertical-wall-kit.jpg', is_kit=True),
    
    Product(name='Medicinal Herbs Growing Kit', category=kits, category_type='kits', price_inr=1799, stock=40,
            description='Grow medicinal plants at home: tulsi, aloe vera, pudina, ajwain. Includes seeds, pots, organic soil, and usage guide.',
            tags='kits, medicinal, herbs, ayurvedic', image='products/medicinal-herbs-kit.jpg', is_kit=True),
    
    Product(name='Organic Pest Control Kit', category=kits, category_type='kits', price_inr=1499, stock=50,
            description='Natural pest management: neem oil, garlic spray, sticky traps, and beneficial insect attractants.',
            tags='kits, pest-control, organic, natural', image='products/pest-control-kit.jpg', is_kit=True),
    
    Product(name='Composting Starter Kit', category=kits, category_type='kits', price_inr=2199, stock=30,
            description='Start composting easily! 50L compost bin, coir bedding, compost accelerator, and step-by-step guide.',
            tags='kits, compost, organic, eco', image='products/compost-starter-kit.jpg', is_kit=True),
    
    Product(name='Butterfly & Bee Garden Kit', category=kits, category_type='kits', price_inr=1899, stock=35,
            description='Attract pollinators with butterfly bush, zinnia, marigold, sunflower seeds, and pollinator house.',
            tags='kits, butterfly, bees, pollinators', image='products/butterfly-garden-kit.jpg', is_kit=True),
    
    Product(name='Indoor Air Purifier Plant Kit', category=kits, category_type='kits', price_inr=2499, stock=40,
            description='NASA-recommended air-purifying plants: snake plant, spider plant, peace lily with decorative pots.',
            tags='kits, indoor, air-purifier, health', image='products/air-purifier-kit.jpg', is_kit=True),
    
    # PREMIUM SOILS & AMENDMENTS (8 items)
    Product(name='Cactus & Succulent Special Mix 3kg', category=soil, category_type='soil', price_inr=399, stock=70,
            description='Fast-draining mix with sand, perlite, and grit. Perfect pH for cacti and succulents.',
            tags='soil, cactus, succulent, special', image='products/cactus-mix.jpg'),
    
    Product(name='Orchid Potting Mix - Premium 2kg', category=soil, category_type='soil', price_inr=549, stock=50,
            description='Specialized orchid mix with bark chips, charcoal, and perlite for excellent drainage and aeration.',
            tags='soil, orchid, premium, special', image='products/orchid-mix.jpg'),
    
    Product(name='Seed Starting Mix - Sterile 5kg', category=soil, category_type='soil', price_inr=449, stock=80,
            description='Sterile, fine-textured mix perfect for seed germination. Disease-free and nutrient-balanced.',
            tags='soil, seeds, sterile, germination', image='products/seed-starting-mix.jpg'),
    
    Product(name='Rose Special Soil Mix 5kg', category=soil, category_type='soil', price_inr=599, stock=60,
            description='Enriched with bone meal and cow manure. Optimal pH for vibrant roses and flowering plants.',
            tags='soil, roses, flowers, enriched', image='products/rose-soil.jpg'),
    
    Product(name='Activated Charcoal - 500g', category=soil, category_type='soil', price_inr=299, stock=90,
            description='Horticultural charcoal for terrariums, drainage layer, and odor absorption. Keeps soil fresh.',
            tags='soil, charcoal, terrarium, drainage', image='products/charcoal.jpg'),
    
    Product(name='Vermiculite - Grade 3 (1kg)', category=soil, category_type='soil', price_inr=349, stock=65,
            description='Lightweight mineral for water retention and aeration. Ideal for seed starting and hydroponics.',
            tags='soil, vermiculite, amendment, retention', image='products/vermiculite.jpg'),
    
    Product(name='Bone Meal Organic Fertilizer 1kg', category=soil, category_type='soil', price_inr=299, stock=75,
            description='Slow-release phosphorus source for strong roots and flowering. 100% organic bone meal.',
            tags='fertilizer, bone-meal, organic, phosphorus', image='products/bone-meal.jpg'),
    
    Product(name='Cow Manure - Composted 5kg', category=soil, category_type='soil', price_inr=349, stock=100,
            description='Well-composted cow manure rich in nutrients. Natural soil conditioner and fertilizer.',
            tags='fertilizer, manure, organic, natural', image='products/cow-manure.jpg'),
    
    # SEASONAL & GIFT ITEMS (7 items)
    Product(name='Teachers Day Plant Gift Set', category=gifts, category_type='gifts', price_inr=899, stock=60,
            description='Bamboo plant with "Best Teacher" plaque, decorative pot, and thank you card.',
            tags='gift, teachers-day, appreciation, bamboo', image='products/teacher-gift.jpg', is_gift=True),
    
    Product(name='Friendship Day Succulent Duo', category=gifts, category_type='gifts', price_inr=799, stock=70,
            description='Pair of matching succulents in decorative pots. Perfect friendship gift with care instructions.',
            tags='gift, friendship, succulent, duo', image='products/friendship-gift.jpg', is_gift=True),
    
    Product(name='Office Desk Mini Garden Set', category=gifts, category_type='gifts', price_inr=1199, stock=55,
            description='Complete mini garden for office desks: 3 small plants, pebbles, miniature accessories.',
            tags='gift, office, desk, mini-garden', image='products/office-mini-garden.jpg', is_gift=True),
    
    Product(name='Get Well Soon Plant Gift', category=gifts, category_type='gifts', price_inr=999, stock=45,
            description='Healing aloe vera plant with "Get Well Soon" message card and care guide.',
            tags='gift, get-well, aloe, health', image='products/get-well-gift.jpg', is_gift=True),
    
    Product(name='Ganesh Chaturthi Plant Gift', category=gifts, category_type='gifts', price_inr=1299, stock=50,
            description='Auspicious tulsi plant in brass pot with Ganesha idol and pooja essentials.',
            tags='gift, ganesh-chaturthi, festival, tulsi', image='products/ganesh-gift.jpg', is_gift=True),
    
    Product(name='Holi Color Garden Kit', category=gifts, category_type='gifts', price_inr=1599, stock=40,
            description='Colorful flower seeds (marigold, hibiscus, bougainvillea) with eco-friendly gulal and pots.',
            tags='gift, holi, festival, colorful', image='products/holi-garden-kit.jpg', is_gift=True),
    
    Product(name='Pongal Sugarcane & Plant Gift', category=gifts, category_type='gifts', price_inr=1199, stock=35,
            description='Traditional Pongal gift with sugarcane, turmeric plant, and decorative kolam pot.',
            tags='gift, pongal, festival, traditional', image='products/pongal-gift.jpg', is_gift=True),
]

print(f"\nAdding {len(new_products)} new comprehensive products...")

try:
    Product.objects.bulk_create(new_products)
    print(f"\n✅ Successfully added {len(new_products)} products!")
except Exception as e:
    print(f"\n⚠️ Error: {e}")
    # Try adding one by one
    added = 0
    for product in new_products:
        try:
            product.save()
            added += 1
        except:
            pass
    print(f"✅ Added {added} products successfully")

print(f"Total products now: {Product.objects.count()}")
print("\n📦 New categories added:")
print("   - 15 Advanced Gardening Tools & Accessories")
print("   - 10 Specialized Growing Kits")
print("   - 8 Premium Soils & Amendments")
print("   - 7 Seasonal & Festival Gift Items")
