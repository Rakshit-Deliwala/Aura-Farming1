"""
Populate all AURA FARMING service plans
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import ServicePlan, MaintenancePlan, WorkshopEvent

print("=" * 80)
print("POPULATING AURA FARMING SERVICE PLANS")
print("=" * 80)
print()

# Clear existing data
ServicePlan.objects.all().delete()
MaintenancePlan.objects.all().delete()
WorkshopEvent.objects.all().delete()

# ===== RESIDENTIAL SOLUTIONS =====
print("Creating Residential Solutions...")

residential_plans = [
    {
        'plan_code': 'A1',
        'name': 'Terrace Starter',
        'tagline': 'Perfect for Apartments & Small Balconies',
        'category': 'residential',
        'price_inr': 8000,
        'space_coverage': '50-80 sq. ft',
        'setup_time': '2-3 hours',
        'warranty': '30 days plant replacement',
        'description': 'Complete terrace gardening setup for beginners with all essentials included.',
        'includes_json': [
            {'item': 'Vertical Garden Stand', 'quantity': '1 unit', 'spec': '4-tier, powder-coated metal'},
            {'item': 'Grow Bags', 'quantity': '8 pieces', 'spec': '12x12 inches, UV-stabilized'},
            {'item': 'Pots', 'quantity': '6 pieces', 'spec': '8-inch ceramic/plastic'},
            {'item': 'Premium Potting Soil', 'quantity': '20 kg', 'spec': 'Organic, coco-peat mix'},
            {'item': 'Seeds Kit', 'quantity': '8 varieties', 'spec': 'Vegetables + Herbs + Flowers'},
            {'item': 'Organic Fertilizers', 'quantity': '1 kg', 'spec': 'Slow-release granules'},
            {'item': 'Drip Irrigation Kit', 'quantity': '1 set', 'spec': 'Basic, 10-dripper system'},
            {'item': 'Gardening Tools', 'quantity': '5-piece set', 'spec': 'Trowel, pruner, sprayer, etc.'},
            {'item': 'Installation Service', 'quantity': '\u2713', 'spec': 'Professional setup'},
            {'item': '1-month Maintenance', 'quantity': '\u2713', 'spec': 'Weekly visit'},
        ],
        'suitable_plants': 'Mint, Coriander, Spinach, Cherry Tomatoes, Chillies, Marigold, Petunia, Strawberries',
        'ideal_for': '1-2 BHK Apartments, Rented accommodations, First-time gardeners',
        'is_featured': True,
        'display_order': 1,
    },
    {
        'plan_code': 'A2',
        'name': 'Balcony Delight',
        'tagline': 'Enhanced Garden for Dedicated Hobbyists',
        'category': 'residential',
        'price_inr': 15000,
        'space_coverage': '100-150 sq. ft',
        'setup_time': '4-5 hours',
        'warranty': '60 days plant replacement',
        'description': 'Premium balcony garden with advanced features for gardening enthusiasts.',
        'includes_json': [
            {'item': 'Wall-Mounted Planters', 'quantity': '10 units', 'spec': '12-inch, self-watering'},
            {'item': 'Floor Planters', 'quantity': '6 units', 'spec': '14-inch, premium finish'},
            {'item': 'Hanging Baskets', 'quantity': '4 units', 'spec': '10-inch with coconut liner'},
            {'item': 'Premium Potting Mix', 'quantity': '40 kg', 'spec': 'Custom blend with vermicompost'},
            {'item': 'Seeds & Saplings', 'quantity': '15 varieties', 'spec': 'Vegetable + Flower + Fruit'},
            {'item': 'Organic NPK Fertilizers', 'quantity': '2 kg', 'spec': 'Complete nutrition pack'},
            {'item': 'Advanced Drip System', 'quantity': '1 set', 'spec': '20-dripper, timer controlled'},
            {'item': 'LED Grow Light', 'quantity': '1 unit', 'spec': '20W, full spectrum'},
            {'item': 'Professional Tool Kit', 'quantity': '8-piece set', 'spec': 'Ergonomic, stainless steel'},
            {'item': 'Decorative Pebbles', 'quantity': '10 kg', 'spec': '2 colors (white/grey)'},
            {'item': 'Installation Service', 'quantity': '\u2713', 'spec': 'Professional setup'},
            {'item': '2-month Maintenance', 'quantity': '\u2713', 'spec': 'Bi-weekly visits'},
            {'item': 'Mobile App Access', 'quantity': '\u2713', 'spec': 'Premium subscription - 3 months'},
        ],
        'suitable_plants': 'All herbs (Basil, Rosemary, Thyme), Leafy greens (Lettuce, Kale, Swiss Chard), Flowering plants (Rose, Jasmine, Hibiscus), Dwarf fruit varieties (Lemon, Pomegranate)',
        'ideal_for': '2-3 BHK Apartments, Dedicated gardening enthusiasts, Families with children',
        'is_featured': True,
        'display_order': 2,
    },
    {
        'plan_code': 'A3',
        'name': 'Villa Premium',
        'tagline': 'Luxury Landscape for Independent Homes',
        'category': 'residential',
        'price_inr': 25000,
        'price_max_inr': 35000,
        'space_coverage': '300-500 sq. ft',
        'setup_time': '1-2 days',
        'warranty': '90 days plant replacement',
        'description': 'Luxury landscaping solution for villas and independent homes with premium features.',
        'includes_json': [
            {'item': 'Raised Garden Beds', 'quantity': '4 units', 'spec': 'Cedar wood, 4x4 ft'},
            {'item': 'Premium Ceramic Pots', 'quantity': '10 units', 'spec': 'Assorted sizes, handcrafted'},
            {'item': 'Decorative Planters', 'quantity': '6 units', 'spec': 'Fiberstone, modern design'},
            {'item': 'Trellis Systems', 'quantity': '2 units', 'spec': 'Metal, 6 ft height'},
            {'item': 'Premium Soil Blend', 'quantity': '200 kg', 'spec': 'Custom formulation'},
            {'item': 'Mature Plants', 'quantity': '20 units', 'spec': '6-month old, flowering/fruiting'},
            {'item': 'Seeds Collection', 'quantity': '25 varieties', 'spec': 'Heirloom, organic'},
            {'item': 'Complete Fertilizer Kit', 'quantity': '6 months supply', 'spec': 'Organic + Bio-stimulants'},
            {'item': 'Smart Irrigation System', 'quantity': 'Full setup', 'spec': 'Wi-Fi controlled, weather-based'},
            {'item': 'Landscape Lighting', 'quantity': '8 units', 'spec': 'Solar-powered, motion sensor'},
            {'item': 'Garden Furniture Set', 'quantity': '1 set', 'spec': '2 chairs + table, weatherproof'},
            {'item': 'Professional Tool Kit', 'quantity': '12-piece set', 'spec': 'Premium brand'},
            {'item': 'Decorative Elements', 'quantity': 'As per design', 'spec': 'Fountains, statues, pathways'},
            {'item': 'Installation Service', 'quantity': '\u2713', 'spec': 'Expert landscape team'},
            {'item': '3-month Maintenance', 'quantity': '\u2713', 'spec': 'Weekly professional care'},
            {'item': 'Mobile App Access', 'quantity': '\u2713', 'spec': 'Premium subscription - 6 months'},
            {'item': 'Consultation Session', 'quantity': '2 sessions', 'spec': 'With senior horticulturist'},
        ],
        'suitable_plants': 'Fruit trees (Dwarf mango, Guava, Citrus), Ornamentals (Bonsai, Ferns, Palms), Flowering shrubs (Hibiscus, Ixora, Bougainvillea), Vegetable garden (Tomatoes, Brinjal, Beans, Cucumber), Medicinal plants (Tulsi, Aloe vera, Curry leaf)',
        'ideal_for': 'Villas and independent homes, Premium residential complexes, Garden party venues',
        'is_featured': True,
        'display_order': 3,
    },
]

for plan in residential_plans:
    ServicePlan.objects.create(**plan)
    print(f"\u2713 Created: {plan['plan_code']} - {plan['name']}")

# ===== CORPORATE SOLUTIONS =====
print("\nCreating Corporate Solutions...")

corporate_plans = [
    {
        'plan_code': 'C1',
        'name': 'Office Oasis',
        'tagline': 'Biophilic Design for Workplaces',
        'category': 'corporate',
        'price_inr': 50000,
        'price_max_inr': 75000,
        'space_coverage': '500-1,000 sq. ft',
        'setup_time': '2-3 days',
        'warranty': 'Maintenance Contract \u20b95,000/month (optional)',
        'description': 'Transform your workplace with biophilic design elements and air-purifying plants.',
        'includes_json': [
            {'item': 'Reception Living Wall', 'quantity': '8x6 ft', 'spec': 'Modular panel system'},
            {'item': 'Desk Plants', 'quantity': '20 units', 'spec': 'Low-maintenance varieties'},
            {'item': 'Floor Planters', 'quantity': '10 units', 'spec': 'Large format'},
            {'item': 'Air-Purifying Plants', 'quantity': 'Selection', 'spec': '15+ varieties'},
            {'item': 'Self-Watering Systems', 'quantity': 'Automated', 'spec': '3-week capacity'},
            {'item': 'LED Plant Lighting', 'quantity': 'Full spectrum', 'spec': 'Timer controlled'},
            {'item': 'Decorative Containers', 'quantity': 'Premium', 'spec': 'Matte finish'},
            {'item': 'Installation & Styling', 'quantity': '\u2713', 'spec': 'Professional interior landscaping'},
            {'item': 'Plant Health Card', 'quantity': 'Quarterly', 'spec': 'Health assessment'},
            {'item': 'Employee Engagement Kit', 'quantity': '\u2713', 'spec': 'Plant care guides, workshops'},
        ],
        'suitable_plants': 'Snake Plant, ZZ Plant, Pothos, Peace Lily, Areca Palm, Ficus, Monstera, Philodendron, Dracaena',
        'ideal_for': 'Corporate offices, Co-working spaces, Banks and financial institutions',
        'display_order': 1,
    },
    {
        'plan_code': 'C2',
        'name': 'Hotel Haven',
        'tagline': 'Hospitality-Grade Landscaping',
        'category': 'corporate',
        'price_inr': 150000,
        'price_max_inr': 300000,
        'space_coverage': '2,000-5,000 sq. ft',
        'setup_time': '5-7 days',
        'warranty': 'Maintenance Contract \u20b915,000-25,000/month',
        'description': 'Premium landscaping solutions for hotels and hospitality venues.',
        'includes_json': [
            {'item': 'Lobby Statement Garden', 'quantity': 'Custom', 'spec': 'Water feature integration'},
            {'item': 'Outdoor Terrace Garden', 'quantity': 'Container', 'spec': 'With seating integration'},
            {'item': 'Indoor Vertical Gardens', 'quantity': '3-5', 'spec': 'Installations'},
            {'item': 'Restaurant Herb Garden', 'quantity': 'Living', 'spec': 'Culinary herb wall'},
            {'item': 'Poolside Planters', 'quantity': 'Weather-resistant', 'spec': 'Tropical varieties'},
            {'item': 'Complete Irrigation System', 'quantity': 'Zone-controlled', 'spec': 'Smart scheduling'},
            {'item': 'Landscape Lighting', 'quantity': 'Architectural', 'spec': 'Accent lighting'},
            {'item': 'Seasonal Flower Rotation', 'quantity': '4 changes', 'spec': 'Per year'},
            {'item': 'Staff Training', 'quantity': 'Basic', 'spec': 'Plant care certification'},
            {'item': 'Emergency Support', 'quantity': '24/7', 'spec': 'Response team'},
        ],
        'ideal_for': 'Hotels and resorts, Fine dining restaurants, Boutique properties',
        'display_order': 2,
    },
    {
        'plan_code': 'C3',
        'name': 'School Green',
        'tagline': 'Educational Garden Program',
        'category': 'corporate',
        'price_inr': 80000,
        'price_max_inr': 120000,
        'space_coverage': '1,000-2,000 sq. ft',
        'setup_time': '3-4 days',
        'warranty': 'Educational Program \u20b98,000/month',
        'description': 'Interactive educational gardens for schools with comprehensive learning programs.',
        'includes_json': [
            {'item': 'Vegetable Garden Beds', 'quantity': '6 raised beds', 'spec': 'Child-friendly height'},
            {'item': 'Sensory Garden', 'quantity': 'Plants', 'spec': 'Touch, smell, taste, sight'},
            {'item': 'Butterfly Garden', 'quantity': 'Nectar', 'spec': 'Host plants'},
            {'item': 'Compost Corner', 'quantity': 'Vermicomposting', 'spec': 'Demonstration unit'},
            {'item': 'Rainwater Harvesting', 'quantity': 'Mini', 'spec': 'Demonstration system'},
            {'item': 'Seed Bank', 'quantity': '50+ varieties', 'spec': 'Storage unit'},
            {'item': 'Gardening Tools', 'quantity': '20 sets', 'spec': 'Child-sized'},
            {'item': 'Curriculum Integration', 'quantity': 'Class-wise', 'spec': 'Activity plans'},
            {'item': 'Teacher Training', 'quantity': '2-day', 'spec': 'Workshop'},
            {'item': 'Student Workshops', 'quantity': '4 sessions', 'spec': 'Per year'},
            {'item': 'Parent Engagement', 'quantity': 'Quarterly', 'spec': 'Gardening days'},
        ],
        'ideal_for': 'Schools and preschools, Educational institutions, Summer camp programs',
        'display_order': 3,
    },
]

for plan in corporate_plans:
    ServicePlan.objects.create(**plan)
    print(f"\u2713 Created: {plan['plan_code']} - {plan['name']}")

# ===== INSTITUTIONAL & GOVERNMENT =====
print("\nCreating Institutional & Government Solutions...")

institutional_plans = [
    {
        'plan_code': 'G1',
        'name': 'Public Garden',
        'tagline': 'Community Green Spaces',
        'category': 'institutional',
        'price_inr': 200000,
        'price_max_inr': 500000,
        'space_coverage': '5,000-20,000 sq. ft',
        'setup_time': '10-15 days',
        'warranty': 'AMC Contract \u20b925,000-50,000/month',
        'description': 'Large-scale landscaping for public parks and community spaces.',
        'includes_json': [
            {'item': 'Mass Plantation', 'quantity': '500-2,000', 'spec': 'Plants'},
            {'item': 'Shade Trees', 'quantity': '20-50', 'spec': 'Units'},
            {'item': 'Flowering Shrubs', 'quantity': '100-300', 'spec': 'Units'},
            {'item': 'Ground Cover', 'quantity': '500-2,000', 'spec': 'Sq. ft'},
            {'item': 'Irrigation Infrastructure', 'quantity': 'Complete', 'spec': 'Piping network'},
            {'item': 'Pathway Development', 'quantity': 'Permeable', 'spec': 'Paving'},
            {'item': 'Sitting Areas', 'quantity': 'Benches', 'spec': 'Shade structures'},
            {'item': 'Signage System', 'quantity': 'Botanical', 'spec': 'Names, QR codes'},
            {'item': 'Maintenance Plan', 'quantity': '3-year', 'spec': 'AMC option'},
        ],
        'ideal_for': 'Municipal gardens, Parks and recreation areas, Traffic islands and medians',
        'display_order': 1,
    },
    {
        'plan_code': 'G2',
        'name': 'Smart City Greenery',
        'tagline': 'Urban Forestry Initiative',
        'category': 'institutional',
        'price_inr': 500000,
        'space_coverage': 'Custom',
        'setup_time': '15-30 days',
        'warranty': 'AMC Contract - Negotiable',
        'description': 'Large-scale urban forestry and smart city green infrastructure projects.',
        'includes_json': [
            {'item': 'Miyawaki Forests', 'quantity': 'Dense', 'spec': 'Native afforestation'},
            {'item': 'Vertical Gardens on Flyovers', 'quantity': 'Large-scale', 'spec': 'Installations'},
            {'item': 'Rooftop Gardens', 'quantity': 'Public Buildings', 'spec': 'Insulation + greenery'},
            {'item': 'Smart Irrigation', 'quantity': 'IoT-enabled', 'spec': 'Water management'},
            {'item': 'Monitoring Dashboard', 'quantity': 'Real-time', 'spec': 'Plant health tracking'},
            {'item': 'Citizen Participation Module', 'quantity': 'Community', 'spec': 'Planting events'},
            {'item': 'Carbon Credit Documentation', 'quantity': 'Sustainability', 'spec': 'Reporting'},
        ],
        'ideal_for': 'Smart city projects, Municipal corporations, Urban development authorities',
        'display_order': 2,
    },
]

for plan in institutional_plans:
    ServicePlan.objects.create(**plan)
    print(f"\u2713 Created: {plan['plan_code']} - {plan['name']}")

print("\n" + "=" * 80)
print("Service Plans: COMPLETED")
print("=" * 80)
print()

# Continue in next part...
print("Run populate_maintenance_plans.py for maintenance plans...")
print("Run populate_workshops.py for workshop events...")
