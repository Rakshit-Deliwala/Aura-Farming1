"""
Populate maintenance plans and workshops
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aura_farming.settings')
django.setup()

from shop.models import MaintenancePlan, WorkshopEvent

print("=" * 80)
print("POPULATING MAINTENANCE PLANS & WORKSHOPS")
print("=" * 80)
print()

# ===== MAINTENANCE PLANS =====
print("Creating Maintenance Plans...")

maintenance_plans = [
    # M1 - Basic Care
    {
        'plan_code': 'M1-MONTHLY',
        'name': 'Basic Care',
        'description': 'Essential Plant Maintenance',
        'billing_period': 'monthly',
        'price_inr': 1500,
        'savings_percentage': 0,
        'visit_frequency': 'Weekly',
        'response_time': '48 hours',
        'services_json': [
            {'service': 'Plant Health Check', 'frequency': 'Weekly'},
            {'service': 'Watering (if automated)', 'frequency': 'Remote monitoring'},
            {'service': 'Pruning & Trimming', 'frequency': 'Bi-weekly'},
            {'service': 'Fertilizer Application', 'frequency': 'Monthly'},
            {'service': 'Pest Control - Basic', 'frequency': 'Monthly'},
            {'service': 'Dead Leaf Removal', 'frequency': 'Weekly'},
            {'service': 'Status Report', 'frequency': 'Monthly via app'},
        ],
        'display_order': 1,
    },
    {
        'plan_code': 'M1-QUARTERLY',
        'name': 'Basic Care',
        'description': 'Essential Plant Maintenance',
        'billing_period': 'quarterly',
        'price_inr': 4200,
        'savings_percentage': 7,
        'visit_frequency': 'Weekly',
        'response_time': '48 hours',
        'services_json': [
            {'service': 'Plant Health Check', 'frequency': 'Weekly'},
            {'service': 'Watering (if automated)', 'frequency': 'Remote monitoring'},
            {'service': 'Pruning & Trimming', 'frequency': 'Bi-weekly'},
            {'service': 'Fertilizer Application', 'frequency': 'Monthly'},
            {'service': 'Pest Control - Basic', 'frequency': 'Monthly'},
            {'service': 'Dead Leaf Removal', 'frequency': 'Weekly'},
            {'service': 'Status Report', 'frequency': 'Monthly via app'},
        ],
        'display_order': 2,
    },
    {
        'plan_code': 'M1-ANNUAL',
        'name': 'Basic Care',
        'description': 'Essential Plant Maintenance',
        'billing_period': 'annual',
        'price_inr': 16000,
        'savings_percentage': 11,
        'visit_frequency': 'Weekly',
        'response_time': '48 hours',
        'services_json': [
            {'service': 'Plant Health Check', 'frequency': 'Weekly'},
            {'service': 'Watering (if automated)', 'frequency': 'Remote monitoring'},
            {'service': 'Pruning & Trimming', 'frequency': 'Bi-weekly'},
            {'service': 'Fertilizer Application', 'frequency': 'Monthly'},
            {'service': 'Pest Control - Basic', 'frequency': 'Monthly'},
            {'service': 'Dead Leaf Removal', 'frequency': 'Weekly'},
            {'service': 'Status Report', 'frequency': 'Monthly via app'},
        ],
        'display_order': 3,
    },
    # M2 - Comprehensive Care
    {
        'plan_code': 'M2-MONTHLY',
        'name': 'Comprehensive Care',
        'description': 'Premium Maintenance Service',
        'billing_period': 'monthly',
        'price_inr': 2800,
        'savings_percentage': 0,
        'visit_frequency': 'Weekly',
        'response_time': '24 hours',
        'services_json': [
            {'service': 'All Basic Care Services', 'frequency': 'As per M1'},
            {'service': 'Plant Rejuvenation Therapy', 'frequency': 'Quarterly'},
            {'service': 'Soil Health Check', 'frequency': 'Quarterly'},
            {'service': 'Organic Pest Control', 'frequency': 'Bi-weekly'},
            {'service': 'Mulching', 'frequency': 'Bi-monthly'},
            {'service': 'Plant Replacement', 'frequency': 'Up to 10% of plants/quarter'},
            {'service': 'Seasonal Plant Rotation', 'frequency': '2 times/year'},
            {'service': 'Expert Consultation', 'frequency': 'Quarterly'},
            {'service': 'Priority Support', 'frequency': '24-hour response'},
        ],
        'display_order': 4,
    },
    {
        'plan_code': 'M2-QUARTERLY',
        'name': 'Comprehensive Care',
        'description': 'Premium Maintenance Service',
        'billing_period': 'quarterly',
        'price_inr': 7800,
        'savings_percentage': 8,
        'visit_frequency': 'Weekly',
        'response_time': '24 hours',
        'services_json': [
            {'service': 'All Basic Care Services', 'frequency': 'As per M1'},
            {'service': 'Plant Rejuvenation Therapy', 'frequency': 'Quarterly'},
            {'service': 'Soil Health Check', 'frequency': 'Quarterly'},
            {'service': 'Organic Pest Control', 'frequency': 'Bi-weekly'},
            {'service': 'Mulching', 'frequency': 'Bi-monthly'},
            {'service': 'Plant Replacement', 'frequency': 'Up to 10% of plants/quarter'},
            {'service': 'Seasonal Plant Rotation', 'frequency': '2 times/year'},
            {'service': 'Expert Consultation', 'frequency': 'Quarterly'},
            {'service': 'Priority Support', 'frequency': '24-hour response'},
        ],
        'display_order': 5,
    },
    {
        'plan_code': 'M2-ANNUAL',
        'name': 'Comprehensive Care',
        'description': 'Premium Maintenance Service',
        'billing_period': 'annual',
        'price_inr': 29500,
        'savings_percentage': 12,
        'visit_frequency': 'Weekly',
        'response_time': '24 hours',
        'services_json': [
            {'service': 'All Basic Care Services', 'frequency': 'As per M1'},
            {'service': 'Plant Rejuvenation Therapy', 'frequency': 'Quarterly'},
            {'service': 'Soil Health Check', 'frequency': 'Quarterly'},
            {'service': 'Organic Pest Control', 'frequency': 'Bi-weekly'},
            {'service': 'Mulching', 'frequency': 'Bi-monthly'},
            {'service': 'Plant Replacement', 'frequency': 'Up to 10% of plants/quarter'},
            {'service': 'Seasonal Plant Rotation', 'frequency': '2 times/year'},
            {'service': 'Expert Consultation', 'frequency': 'Quarterly'},
            {'service': 'Priority Support', 'frequency': '24-hour response'},
        ],
        'display_order': 6,
    },
    # M3 - Corporate Care
    {
        'plan_code': 'M3-MONTHLY',
        'name': 'Corporate Care',
        'description': 'Enterprise-Grade Maintenance',
        'billing_period': 'monthly',
        'price_inr': 5000,
        'savings_percentage': 0,
        'visit_frequency': 'Custom',
        'response_time': '4 hours',
        'services_json': [
            {'service': 'All Comprehensive Care Services', 'frequency': 'As per M2'},
            {'service': 'Dedicated Account Manager', 'frequency': 'Ongoing'},
            {'service': 'Bi-Annual Plant Audit', 'frequency': '2 times/year'},
            {'service': 'Complete Plant Replacement Warranty', 'frequency': '15% annual refresh'},
            {'service': 'Employee Wellness Workshops', 'frequency': 'Quarterly'},
            {'service': 'Emergency Support', 'frequency': '4-hour response'},
            {'service': 'Sustainability Reporting', 'frequency': 'Annual certification'},
        ],
        'display_order': 7,
    },
    {
        'plan_code': 'M3-ANNUAL',
        'name': 'Corporate Care',
        'description': 'Enterprise-Grade Maintenance',
        'billing_period': 'annual',
        'price_inr': 54000,
        'savings_percentage': 10,
        'visit_frequency': 'Custom',
        'response_time': '4 hours',
        'services_json': [
            {'service': 'All Comprehensive Care Services', 'frequency': 'As per M2'},
            {'service': 'Dedicated Account Manager', 'frequency': 'Ongoing'},
            {'service': 'Bi-Annual Plant Audit', 'frequency': '2 times/year'},
            {'service': 'Complete Plant Replacement Warranty', 'frequency': '15% annual refresh'},
            {'service': 'Employee Wellness Workshops', 'frequency': 'Quarterly'},
            {'service': 'Emergency Support', 'frequency': '4-hour response'},
            {'service': 'Sustainability Reporting', 'frequency': 'Annual certification'},
        ],
        'display_order': 8,
    },
]

for plan in maintenance_plans:
    MaintenancePlan.objects.create(**plan)
    print(f"\u2713 Created: {plan['plan_code']} - {plan['name']} ({plan['billing_period']})")

# ===== WORKSHOPS & EVENTS =====
print("\nCreating Workshop Events...")

workshops = [
    # Hobby Workshops (W1)
    {
        'name': 'Kitchen Gardening 101',
        'event_type': 'hobby',
        'duration': '3 hours',
        'price_per_person': 1200,
        'min_group_size': 10,
        'max_group_size': 20,
        'description': 'Learn the basics of growing your own vegetables and herbs at home.',
        'includes': 'Training materials, starter seed kit, refreshments, certificate',
    },
    {
        'name': 'Terrace Garden Planning',
        'event_type': 'hobby',
        'duration': '4 hours',
        'price_per_person': 1800,
        'min_group_size': 8,
        'max_group_size': 15,
        'description': 'Complete guide to designing and setting up a terrace garden.',
        'includes': 'Design template, plant selection guide, site assessment checklist, refreshments',
    },
    {
        'name': 'Organic Pest Control',
        'event_type': 'hobby',
        'duration': '2 hours',
        'price_per_person': 900,
        'min_group_size': 10,
        'max_group_size': 25,
        'description': 'Natural methods to protect your plants from pests and diseases.',
        'includes': 'Recipe handbook, organic spray samples, plant health guide',
    },
    {
        'name': 'Bonsai Making',
        'event_type': 'hobby',
        'duration': '5 hours',
        'price_per_person': 2500,
        'min_group_size': 5,
        'max_group_size': 10,
        'description': 'Hands-on bonsai creation workshop with expert guidance.',
        'includes': 'Bonsai plant, pot, tools, training wire, lunch, certificate',
    },
    {
        'name': 'Terrarium Workshop',
        'event_type': 'hobby',
        'duration': '2 hours',
        'price_per_person': 1500,
        'min_group_size': 8,
        'max_group_size': 15,
        'description': 'Create your own mini garden in a glass container.',
        'includes': 'Glass container, plants, decorative elements, care guide',
    },
    {
        'name': 'Kokedama Workshop',
        'event_type': 'hobby',
        'duration': '2 hours',
        'price_per_person': 1500,
        'min_group_size': 8,
        'max_group_size': 15,
        'description': 'Learn the Japanese art of moss ball planters.',
        'includes': 'Plant, moss, soil, twine, care instructions',
    },
    # Corporate Workshops (W2)
    {
        'name': 'Team Building Garden Day',
        'event_type': 'corporate',
        'duration': '4 hours',
        'price_per_person': 1250,
        'min_group_size': 15,
        'max_group_size': 20,
        'description': 'Engaging team building activities centered around gardening.',
        'includes': 'Plant session, team activities, take-home plant, refreshments',
    },
    {
        'name': 'Wellness Wednesday Series',
        'event_type': 'corporate',
        'duration': '1 hour/week x 4 weeks',
        'price_per_person': 2000,
        'min_group_size': 10,
        'max_group_size': 30,
        'description': 'Monthly wellness program with plant care and stress relief sessions.',
        'includes': '4 workshops, office plant audit, digital resources',
    },
    {
        'name': 'Leadership Offsite',
        'event_type': 'corporate',
        'duration': '6 hours',
        'price_per_person': 2500,
        'min_group_size': 10,
        'max_group_size': 20,
        'description': 'Leadership development through garden-based activities.',
        'includes': 'Custom garden experience, team challenges, lunch, certificate',
    },
    {
        'name': 'Festival Special',
        'event_type': 'corporate',
        'duration': '3 hours',
        'price_per_person': 1500,
        'min_group_size': 15,
        'max_group_size': 20,
        'description': 'Themed gardening activity for company festivals and celebrations.',
        'includes': 'Festive plants, decorative pots, celebration kit',
    },
]

for workshop in workshops:
    WorkshopEvent.objects.create(**workshop)
    print(f"\u2713 Created: {workshop['name']} - {workshop['event_type']}")

print("\n" + "=" * 80)
print("COMPLETED SUCCESSFULLY!")
print("=" * 80)
print()
print(f"Service Plans: {ServicePlan.objects.count()}")
print(f"Maintenance Plans: {MaintenancePlan.objects.count()}")
print(f"Workshop Events: {WorkshopEvent.objects.count()}")
