from django.db.models.signals import post_migrate
from django.db.utils import OperationalError
from django.dispatch import receiver

from .models import Category, Product


@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name != 'shop':
        return
    try:
        if Category.objects.exists():
            return
    except OperationalError:
        # Tables not created yet (e.g. shop migrations not applied)
        return

    tools = Category.objects.create(name='Gardening Tools & Accessories', slug='tools-accessories')
    kits = Category.objects.create(name='DIY Growing Kits', slug='diy-kits')
    soil = Category.objects.create(name='Organic Fertilizers & Soils', slug='fertilizers-soils')
    gifts = Category.objects.create(name='Eco-Friendly Gifts', slug='eco-gifts')

    Product.objects.bulk_create([
        # TOOLKITS - Main Products (8 varieties)
        Product(name='AURA Premium Gardening Toolkit (8-in-1)', category=tools, category_type='tools', price_inr=1899, stock=50,
                description='Complete professional toolkit with stainless steel trowel, cultivator, weeder, pruner, spray bottle, garden gloves, kneeling pad, and carry bag.', 
                tags='toolkit, beginners, premium, bestseller', is_featured=True, is_kit=True),
        Product(name='Mini Gardening Tool Set (5-in-1)', category=tools, category_type='tools', price_inr=899, stock=80,
                description='Compact toolkit perfect for indoor plants and small gardens. Includes mini trowel, rake, shovel, spray bottle, and pruning shears.',
                tags='toolkit, mini, indoor, compact', is_featured=True, is_kit=True),
        Product(name='AURA Professional Gardening Toolkit (12-in-1)', category=tools, category_type='tools', price_inr=2899, stock=30,
                description='Premium professional toolkit with heavy-duty tools, ergonomic handles, garden scissors, soil tester, plant labels, and premium carry case.',
                tags='toolkit, professional, premium, advanced', is_kit=True),
        Product(name='Kids Gardening Tool Set (6-in-1)', category=tools, category_type='tools', price_inr=699, stock=60,
                description='Safe and colorful gardening set for children. Includes child-sized tools, watering can, gloves, apron, and activity guide.',
                tags='toolkit, kids, children, educational', is_kit=True),
        Product(name='Balcony Gardening Essentials Kit', category=tools, category_type='tools', price_inr=1499, stock=45,
                description='Everything needed for balcony gardening: railing planters, vertical garden kit, drip trays, hooks, and basic tools.',
                tags='toolkit, balcony, urban, space-saving', is_kit=True),
        Product(name='Terrace Gardening Master Kit', category=tools, category_type='tools', price_inr=3499, stock=25,
                description='Complete terrace setup: large grow bags, drip irrigation system, vertical structures, premium soil mix, and tool set.',
                tags='toolkit, terrace, advanced, complete', is_kit=True),
        Product(name='Bonsai Care Toolkit (7-in-1)', category=tools, category_type='tools', price_inr=1299, stock=40,
                description='Specialized bonsai tools: concave cutters, wire cutters, root rake, trimming scissors, training wire, and care guide.',
                tags='toolkit, bonsai, specialized, premium', is_kit=True),
        Product(name='Organic Farming Starter Kit', category=tools, category_type='tools', price_inr=1999, stock=35,
                description='Begin organic farming with vermicompost setup, organic seeds, neem spray, and essential tools.',
                tags='toolkit, organic, farming, natural', is_kit=True),
        
        # INDIVIDUAL TOOLS & ACCESSORIES (10 items)
        Product(name='Stainless Steel Hand Trowel', category=tools, category_type='tools', price_inr=299, stock=100,
                description='Durable stainless steel trowel with ergonomic wooden handle. Perfect for digging, planting, and transplanting.',
                tags='tools, trowel, steel, individual'),
        Product(name='Pruning Secateurs  - Professional Grade', category=tools, category_type='tools', price_inr=599, stock=70,
                description='Sharp Japanese steel pruning shears with safety lock and comfortable grip. Ideal for roses, shrubs, and fruit trees.',
                tags='tools, pruner, secateurs, professional'),
        Product(name='Garden Gloves - Anti-Cut Protection', category=tools, category_type='tools', price_inr=349, stock=120,
                description='Breathable anti-cut gloves with touchscreen fingertips. Available in S, M, L sizes.',
                tags='tools, gloves, protection, safety'),
        Product(name='Watering Can with Long Spout - 5L', category=tools, category_type='tools', price_inr=449, stock=60,
                description='Rust-proof 5-liter watering can with detachable rose head for gentle watering.',
                tags='tools, watering, can, essential'),
        Product(name='Soil pH Tester - 3-in-1', category=tools, category_type='tools', price_inr=799, stock=50,
                description='Digital soil tester measures pH, moisture, and light levels. No batteries required.',
                tags='tools, tester, pH, technology'),
        Product(name='Vertical Wall Planter Set (6 pockets)', category=tools, category_type='tools', price_inr=899, stock=40,
                description='Space-saving felt wall planter with 6 pockets. Perfect for herbs and succulents.',
                tags='tools, vertical, wall, planter'),
        Product(name='Drip Irrigation Kit for 25 Plants', category=tools, category_type='tools', price_inr=1299, stock=35,
                description='Automated drip system with timer, 25m tubing, and adjustable drippers.',
                tags='tools, irrigation, drip, automated'),
        Product(name='Grow Bags Set - 5 Pack (12"×12")', category=tools, category_type='tools', price_inr=599, stock=80,
                description='Premium breathable fabric grow bags with handles. Perfect for vegetables and flowers.',
                tags='tools, grow-bags, fabric, reusable'),
        Product(name='Garden Kneeler & Seat 2-in-1', category=tools, category_type='tools', price_inr=1499, stock=30,
                description='Foldable garden stool with tool pouch. Flip for kneeling pad or sitting.',
                tags='tools, kneeler, seat, comfort'),
        Product(name='Compost Bin - 50L Capacity', category=tools, category_type='tools', price_inr=1799, stock=25,
                description='Compact compost bin with aeration holes and harvest door. Perfect for home composting.',
                tags='tools, compost, organic, eco'),
        
        # DIY GROWING KITS (8 varieties)
        Product(name='Beginner Balcony Farming Kit', category=kits, category_type='kits', price_inr=2499, stock=40,
                description='Complete starter kit with 5 grow bags, cocopeat, organic potting mix, seasonal vegetable seeds (tomato, chilli, coriander, mint), and setup guide.',
                tags='balcony, kit, beginners, vegetables', is_featured=True, is_kit=True),
        Product(name='Microgreens DIY Kit – 5 Varieties', category=kits, category_type='kits', price_inr=1299, stock=60,
                description='Microgreens tray with drainage, coir mat, spray bottle, seed packs of sunflower, radish, broccoli, wheatgrass, mustard with detailed growing guide.',
                tags='microgreens, kit, indoor, healthy', is_kit=True),
        Product(name='Herb Garden Kit - Kitchen Essentials', category=kits, category_type='kits', price_inr=1599, stock=55,
                description='Grow fresh herbs at home! Includes basil, coriander, mint, parsley seeds, 4 ceramic pots, soil mix, and care instructions.',
                tags='herbs, kit, kitchen, cooking', is_featured=True, is_kit=True),
        Product(name='Flower Gardening Kit - Seasonal Blooms', category=kits, category_type='kits', price_inr=1899, stock=45,
                description='Create a colorful garden with marigold, zinnia, sunflower, petunia seeds, grow bags, and organic fertilizer.',
                tags='flowers, kit, colorful, seasonal', is_kit=True),
        Product(name='Mushroom Growing Kit - Oyster Variety', category=kits, category_type='kits', price_inr=1799, stock=30,
                description='Grow fresh mushrooms at home! Pre-colonized substrate, spray bottle, and complete growing instructions.',
                tags='mushroom, kit, exotic, unique', is_kit=True),
        Product(name='Cactus & Succulent Garden Kit', category=kits, category_type='kits', price_inr=1199, stock=50,
                description='Low-maintenance kit with 5 succulent varieties, decorative pots, specialized soil mix, and pebbles.',
                tags='cactus, succulent, kit, low-maintenance', is_kit=True),
        Product(name='Kids Vegetable Growing Kit', category=kits, category_type='kits', price_inr=999, stock=65,
                description='Educational kit for children with easy-to-grow vegetables, colorful planters, seed labels, and activity book.',
                tags='kids, vegetables, kit, educational', is_kit=True),
        Product(name='Indoor Hydroponic Growing System', category=kits, category_type='kits', price_inr=3999, stock=20,
                description='Modern hydroponic system with LED grow light, nutrient solution, and seeds for lettuce, herbs, and greens.',
                tags='hydroponic, kit, indoor, technology', is_kit=True),
        
        # SOIL & FERTILIZERS (8 varieties)
        Product(name='Organic Vegetable Potting Mix 10kg', category=soil, category_type='soil', price_inr=499, stock=100,
                description='Premium blend of cocopeat, vermicompost, neem cake, and perlite. Perfect for chemical-free vegetables.',
                tags='soil, organic, vegetables, premium', is_featured=True),
        Product(name='Cocopeat Block - Expands to 5kg', category=soil, category_type='soil', price_inr=299, stock=150,
                description='Compressed cocopeat block. Eco-friendly alternative to peat moss. Excellent water retention.',
                tags='soil, cocopeat, organic, sustainable'),
        Product(name='Vermicompost - Premium Quality 5kg', category=soil, category_type='soil', price_inr=399, stock=120,
                description='Rich organic manure from earthworms. Improves soil structure and plant nutrition.',
                tags='soil, vermicompost, organic, fertilizer'),
        Product(name='Neem Cake Organic Fertilizer 2kg', category=soil, category_type='soil', price_inr=299, stock=80,
                description='Natural pest repellent and soil conditioner. Slow-release organic nitrogen source.',
                tags='soil, neem, organic, pest-control'),
        Product(name='All-Purpose Flower Potting Mix 5kg', category=soil, category_type='soil', price_inr=349, stock=90,
                description='Specially formulated for flowering plants with bone meal and essential minerals.',
                tags='soil, flowers, potting-mix, nourishing'),
        Product(name='Perlite - Soil Amendment 1kg', category=soil, category_type='soil', price_inr=249, stock=70,
                description='Volcanic glass for improved drainage and aeration. Essential for succulents and orchids.',
                tags='soil, perlite, amendment, drainage'),
        Product(name='Organic Seaweed Liquid Fertilizer 500ml', category=soil, category_type='soil', price_inr=449, stock=60,
                description='Concentrated seaweed extract rich in micronutrients. Dilute and spray for healthier growth.',
                tags='fertilizer, liquid, seaweed, organic'),
        Product(name='Complete NPK Fertilizer - Organic 1kg', category=soil, category_type='soil', price_inr=399, stock=85,
                description='Balanced N-P-K fertilizer for all plants. Slow-release organic granules.',
                tags='fertilizer, npk, organic, complete'),
        
        # ECO-FRIENDLY GIFTS (12 varieties including seasonal, corporate, festival)
        Product(name='Rakhi Eco-Gift Hamper with Plantable Seeds', category=gifts, category_type='gifts', price_inr=999, stock=80,
                description='Special Rakhi gift with plantable seed rakhi, cocopeat coin, biodegradable pot with flower seeds, and greeting card.',
                tags='rakhi, eco, gift, festival, seeds', is_gift=True, is_featured=True),
        Product(name='Diwali Green Gift Box - Temple Plants', category=gifts, category_type='gifts', price_inr=1499, stock=70,
                description='Auspicious gift set with tulsi plant, brass diya planter, camphor oil, and organic incense sticks.',
                tags='diwali, festival, eco, gift, traditional', is_gift=True),
        Product(name='Corporate Desk Garden Gift Box', category=gifts, category_type='gifts', price_inr=1499, stock=50,
                description='Professional gift with money plant in ceramic planter, bamboo pen stand, and plant care card.',
                tags='corporate, gift, desk, professional', is_gift=True),
        Product(name='Birthday Terrarium Gift Kit', category=gifts, category_type='gifts', price_inr=1299, stock=60,
                description='DIY terrarium kit with glass jar, succulents, colored stones, miniature accessories, and birthday card.',
                tags='birthday, gift, terrarium, diy', is_gift=True),
        Product(name='Wedding Return Gift - Plant Saplings (Set of 25)', category=gifts, category_type='gifts', price_inr=2499, stock=40,
                description='Eco-friendly wedding favors with 25 saplings in jute bags, personalized tags, and care instructions.',
                tags='wedding, bulk, gift, eco, saplings', is_gift=True),
        Product(name='Mothers Day Special - Rose Plant Gift', category=gifts, category_type='gifts', price_inr=1199, stock=65,
                description='Live rose plant in decorative ceramic pot with "Best Mom" plaque and care guide.',
                tags='mothers-day, gift, roses, special', is_gift=True),
        Product(name='Valentine Love Plant Combo', category=gifts, category_type='gifts', price_inr=1599, stock=55,
                description='Romantic gift set with 2 lucky bamboo in heart-shaped pot, scented candle, and love note holder.',
                tags='valentine, gift, romantic, couple', is_gift=True),
        Product(name='New Home Blessing Plant Set', category=gifts, category_type='gifts', price_inr=1899, stock=45,
                description='Housewarming gift with money plant, peace lily, ceramic planters, and "New Home" greeting.',
                tags='housewarming, gift, blessing, new-home', is_gift=True),
        Product(name='Corporate Bulk Order - Desk Plants (Set of 50)', category=gifts, category_type='gifts', price_inr=14999, stock=10,
                description='Economical bulk order for corporate gifting. 50 low-maintenance desk plants with branded tags.',
                tags='corporate, bulk, gift, economy', is_gift=True),
        Product(name='Christmas Green Gift Hamper', category=gifts, category_type='gifts', price_inr=1699, stock=60,
                description='Festive hamper with mini Christmas tree plant, decorative pot, fairy lights, and eco-friendly wrapping.',
                tags='christmas, festival, gift, festive', is_gift=True),
        Product(name='Thank You Gift - Bamboo Planter Set', category=gifts, category_type='gifts', price_inr=899, stock=75,
                description='Elegant bamboo plant in wooden planter with "Thank You" card. Perfect for appreciation.',
                tags='thank-you, gift, appreciation, bamboo', is_gift=True),
        Product(name='Anniversary Special - Bonsai Gift', category=gifts, category_type='gifts', price_inr=2499, stock=30,
                description='Premium bonsai tree in decorative ceramic pot with care kit and anniversary wishes card.',
                tags='anniversary, gift, bonsai, premium', is_gift=True),
    ])
