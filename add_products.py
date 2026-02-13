"""
Add all new products to database
Run with: python manage.py shell < add_products.py
"""
from shop.models import Category, Product

# Get categories
categories = {cat.slug: cat for cat in Category.objects.all()}
tools = categories.get('tools-accessories')
kits = categories.get('diy-kits')
soil = categories.get('fertilizers-soils')
gifts = categories.get('eco-gifts')

# Check existing products
existing_count = Product.objects.count()
print(f"Existing products: {existing_count}")

# New products to add (excluding existing 6)
new_products = [
    # Toolkits
    Product(name='Mini Gardening Tool Set (5-in-1)', category=tools, category_type='tools', price_inr=899, stock=80,
            description='Compact toolkit perfect for indoor plants and small gardens. Includes mini trowel, rake, shovel, spray bottle, and pruning shears.',
            tags='toolkit, mini, indoor, compact', image='products/mini-tool-set.jpg', is_featured=True, is_kit=True),
    Product(name='AURA Professional Gardening Toolkit (12-in-1)', category=tools, category_type='tools', price_inr=2899, stock=30,
            description='Premium professional toolkit with heavy-duty tools, ergonomic handles, garden scissors, soil tester, plant labels, and premium carry case.',
            tags='toolkit, professional, premium, advanced', image='products/professional-toolkit.jpg', is_kit=True),
    Product(name='Kids Gardening Tool Set (6-in-1)', category=tools, category_type='tools', price_inr=699, stock=60,
            description='Safe and colorful gardening set for children. Includes child-sized tools, watering can, gloves, apron, and activity guide.',
            tags='toolkit, kids, children, educational', image='products/kids-tool-set.jpg', is_kit=True),
    Product(name='Balcony Gardening Essentials Kit', category=tools, category_type='tools', price_inr=1499, stock=45,
            description='Everything needed for balcony gardening: railing planters, vertical garden kit, drip trays, hooks, and basic tools.',
            tags='toolkit, balcony, urban, space-saving', image='products/balcony-essentials.jpg', is_kit=True),
    Product(name='Terrace Gardening Master Kit', category=tools, category_type='tools', price_inr=3499, stock=25,
            description='Complete terrace setup: large grow bags, drip irrigation system, vertical structures, premium soil mix, and tool set.',
            tags='toolkit, terrace, advanced, complete', image='products/terrace-master-kit.jpg', is_kit=True),
    Product(name='Bonsai Care Toolkit (7-in-1)', category=tools, category_type='tools', price_inr=1299, stock=40,
            description='Specialized bonsai tools: concave cutters, wire cutters, root rake, trimming scissors, training wire, and care guide.',
            tags='toolkit, bonsai, specialized, premium', image='products/bonsai-toolkit.jpg', is_kit=True),
    Product(name='Organic Farming Starter Kit', category=tools, category_type='tools', price_inr=1999, stock=35,
            description='Begin organic farming with vermicompost setup, organic seeds, neem spray, and essential tools.',
            tags='toolkit, organic, farming, natural', image='products/organic-farming-kit.jpg', is_kit=True),
    
    # Individual Tools
    Product(name='Stainless Steel Hand Trowel', category=tools, category_type='tools', price_inr=299, stock=100,
            description='Durable stainless steel trowel with ergonomic wooden handle. Perfect for digging, planting, and transplanting.',
            tags='tools, trowel, steel, individual', image='products/hand-trowel.jpg'),
    Product(name='Pruning Secateurs - Professional Grade', category=tools, category_type='tools', price_inr=599, stock=70,
            description='Sharp Japanese steel pruning shears with safety lock and comfortable grip. Ideal for roses, shrubs, and fruit trees.',
            tags='tools, pruner, secateurs, professional', image='products/pruning-secateurs.jpg'),
    Product(name='Garden Gloves - Anti-Cut Protection', category=tools, category_type='tools', price_inr=349, stock=120,
            description='Breathable anti-cut gloves with touchscreen fingertips. Available in S, M, L sizes.',
            tags='tools, gloves, protection, safety', image='products/garden-gloves.jpg'),
    Product(name='Watering Can with Long Spout - 5L', category=tools, category_type='tools', price_inr=449, stock=60,
            description='Rust-proof 5-liter watering can with detachable rose head for gentle watering.',
            tags='tools, watering, can, essential', image='products/watering-can.jpg'),
    Product(name='Soil pH Tester - 3-in-1', category=tools, category_type='tools', price_inr=799, stock=50,
            description='Digital soil tester measures pH, moisture, and light levels. No batteries required.',
            tags='tools, tester, pH, technology', image='products/soil-tester.jpg'),
    Product(name='Vertical Wall Planter Set (6 pockets)', category=tools, category_type='tools', price_inr=899, stock=40,
            description='Space-saving felt wall planter with 6 pockets. Perfect for herbs and succulents.',
            tags='tools, vertical, wall, planter', image='products/wall-planter.jpg'),
    Product(name='Drip Irrigation Kit for 25 Plants', category=tools, category_type='tools', price_inr=1299, stock=35,
            description='Automated drip system with timer, 25m tubing, and adjustable drippers.',
            tags='tools, irrigation, drip, automated', image='products/drip-irrigation.jpg'),
    Product(name='Grow Bags Set - 5 Pack (12"×12")', category=tools, category_type='tools', price_inr=599, stock=80,
            description='Premium breathable fabric grow bags with handles. Perfect for vegetables and flowers.',
            tags='tools, grow-bags, fabric, reusable', image='products/grow-bags.jpg'),
    Product(name='Garden Kneeler & Seat 2-in-1', category=tools, category_type='tools', price_inr=1499, stock=30,
            description='Foldable garden stool with tool pouch. Flip for kneeling pad or sitting.',
            tags='tools, kneeler, seat, comfort', image='products/garden-kneeler.jpg'),
    Product(name='Compost Bin - 50L Capacity', category=tools, category_type='tools', price_inr=1799, stock=25,
            description='Compact compost bin with aeration holes and harvest door. Perfect for home composting.',
            tags='tools, compost, organic, eco', image='products/compost-bin.jpg'),
    
    # DIY Kits
    Product(name='Herb Garden Kit - Kitchen Essentials', category=kits, category_type='kits', price_inr=1599, stock=55,
            description='Grow fresh herbs at home! Includes basil, coriander, mint, parsley seeds, 4 ceramic pots, soil mix, and care instructions.',
            tags='herbs, kit, kitchen, cooking', image='products/herb-garden-kit.jpg', is_featured=True, is_kit=True),
    Product(name='Flower Gardening Kit - Seasonal Blooms', category=kits, category_type='kits', price_inr=1899, stock=45,
            description='Create a colorful garden with marigold, zinnia, sunflower, petunia seeds, grow bags, and organic fertilizer.',
            tags='flowers, kit, colorful, seasonal', image='products/flower-kit.jpg', is_kit=True),
    Product(name='Mushroom Growing Kit - Oyster Variety', category=kits, category_type='kits', price_inr=1799, stock=30,
            description='Grow fresh mushrooms at home! Pre-colonized substrate, spray bottle, and complete growing instructions.',
            tags='mushroom, kit, exotic, unique', image='products/mushroom-kit.jpg', is_kit=True),
    Product(name='Cactus & Succulent Garden Kit', category=kits, category_type='kits', price_inr=1199, stock=50,
            description='Low-maintenance kit with 5 succulent varieties, decorative pots, specialized soil mix, and pebbles.',
            tags='cactus, succulent, kit, low-maintenance', image='products/succulent-kit.jpg', is_kit=True),
    Product(name='Kids Vegetable Growing Kit', category=kits, category_type='kits', price_inr=999, stock=65,
            description='Educational kit for children with easy-to-grow vegetables, colorful planters, seed labels, and activity book.',
            tags='kids, vegetables, kit, educational', image='products/kids-vegetable-kit.jpg', is_kit=True),
    Product(name='Indoor Hydroponic Growing System', category=kits, category_type='kits', price_inr=3999, stock=20,
            description='Modern hydroponic system with LED grow light, nutrient solution, and seeds for lettuce, herbs, and greens.',
            tags='hydroponic, kit, indoor, technology', image='products/hydroponic-system.jpg', is_kit=True),
    
    # Soil & Fertilizers
    Product(name='Cocopeat Block - Expands to 5kg', category=soil, category_type='soil', price_inr=299, stock=150,
            description='Compressed cocopeat block. Eco-friendly alternative to peat moss. Excellent water retention.',
            tags='soil, cocopeat, organic, sustainable', image='products/cocopeat-block.jpg'),
    Product(name='Vermicompost - Premium Quality 5kg', category=soil, category_type='soil', price_inr=399, stock=120,
            description='Rich organic manure from earthworms. Improves soil structure and plant nutrition.',
            tags='soil, vermicompost, organic, fertilizer', image='products/vermicompost.jpg'),
    Product(name='Neem Cake Organic Fertilizer 2kg', category=soil, category_type='soil', price_inr=299, stock=80,
            description='Natural pest repellent and soil conditioner. Slow-release organic nitrogen source.',
            tags='soil, neem, organic, pest-control', image='products/neem-cake.jpg'),
    Product(name='All-Purpose Flower Potting Mix 5kg', category=soil, category_type='soil', price_inr=349, stock=90,
            description='Specially formulated for flowering plants with bone meal and essential minerals.',
            tags='soil, flowers, potting-mix, nourishing', image='products/flower-potting-mix.jpg'),
    Product(name='Perlite - Soil Amendment 1kg', category=soil, category_type='soil', price_inr=249, stock=70,
            description='Volcanic glass for improved drainage and aeration. Essential for succulents and orchids.',
            tags='soil, perlite, amendment, drainage', image='products/perlite.jpg'),
    Product(name='Organic Seaweed Liquid Fertilizer 500ml', category=soil, category_type='soil', price_inr=449, stock=60,
            description='Concentrated seaweed extract rich in micronutrients. Dilute and spray for healthier growth.',
            tags='fertilizer, liquid, seaweed, organic', image='products/seaweed-fertilizer.jpg'),
    Product(name='Complete NPK Fertilizer - Organic 1kg', category=soil, category_type='soil', price_inr=399, stock=85,
            description='Balanced N-P-K fertilizer for all plants. Slow-release organic granules.',
            tags='fertilizer, npk, organic, complete', image='products/npk-fertilizer.jpg'),
    
    # Eco-Friendly Gifts
    Product(name='Diwali Green Gift Box - Temple Plants', category=gifts, category_type='gifts', price_inr=1499, stock=70,
            description='Auspicious gift set with tulsi plant, brass diya planter, camphor oil, and organic incense sticks.',
            tags='diwali, festival, eco, gift, traditional', image='products/diwali-gift.jpg', is_gift=True),
    Product(name='Birthday Terrarium Gift Kit', category=gifts, category_type='gifts', price_inr=1299, stock=60,
            description='DIY terrarium kit with glass jar, succulents, colored stones, miniature accessories, and birthday card.',
            tags='birthday, gift, terrarium, diy', image='products/birthday-terrarium.jpg', is_gift=True),
    Product(name='Wedding Return Gift - Plant Saplings (Set of 25)', category=gifts, category_type='gifts', price_inr=2499, stock=40,
            description='Eco-friendly wedding favors with 25 saplings in jute bags, personalized tags, and care instructions.',
            tags='wedding, bulk, gift, eco, saplings', image='products/wedding-sapling.jpg', is_gift=True),
    Product(name='Mothers Day Special - Rose Plant Gift', category=gifts, category_type='gifts', price_inr=1199, stock=65,
            description='Live rose plant in decorative ceramic pot with "Best Mom" plaque and care guide.',
            tags='mothers-day, gift, roses, special', image='products/mothers-day-rose.jpg', is_gift=True),
    Product(name='Valentine Love Plant Combo', category=gifts, category_type='gifts', price_inr=1599, stock=55,
            description='Romantic gift set with 2 lucky bamboo in heart-shaped pot, scented candle, and love note holder.',
            tags='valentine, gift, romantic, couple', image='products/valentine-combo.jpg', is_gift=True),
    Product(name='New Home Blessing Plant Set', category=gifts, category_type='gifts', price_inr=1899, stock=45,
            description='Housewarming gift with money plant, peace lily, ceramic planters, and "New Home" greeting.',
            tags='housewarming, gift, blessing, new-home', image='products/new-home-set.jpg', is_gift=True),
    Product(name='Corporate Bulk Order - Desk Plants (Set of 50)', category=gifts, category_type='gifts', price_inr=14999, stock=10,
            description='Economical bulk order for corporate gifting. 50 low-maintenance desk plants with branded tags.',
            tags='corporate, bulk, gift, economy', image='products/corporate-bulk.jpg', is_gift=True),
    Product(name='Christmas Green Gift Hamper', category=gifts, category_type='gifts', price_inr=1699, stock=60,
            description='Festive hamper with mini Christmas tree plant, decorative pot, fairy lights, and eco-friendly wrapping.',
            tags='christmas, festival, gift, festive', image='products/christmas-gift.jpg', is_gift=True),
    Product(name='Thank You Gift - Bamboo Planter Set', category=gifts, category_type='gifts', price_inr=899, stock=75,
            description='Elegant bamboo plant in wooden planter with "Thank You" card. Perfect for appreciation.',
            tags='thank-you, gift, appreciation, bamboo', image='products/thank-you-bamboo.jpg', is_gift=True),
    Product(name='Anniversary Special - Bonsai Gift', category=gifts, category_type='gifts', price_inr=2499, stock=30,
            description='Premium bonsai tree in decorative ceramic pot with care kit and anniversary wishes card.',
            tags='anniversary, gift, bonsai, premium', image='products/anniversary-bonsai.jpg', is_gift=True),
]

# Add products
print(f"\nAdding {len(new_products)} new products...")
Product.objects.bulk_create(new_products)

print(f"\n✅ Successfully added {len(new_products)} new products!")
print(f"Total products now: {Product.objects.count()}")
