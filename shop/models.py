from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tools', 'Gardening Tools & Accessories'),
        ('kits', 'DIY Growing Kits'),
        ('soil', 'Organic Fertilizers & Soils'),
        ('gifts', 'Eco-Friendly Gifts'),
    ]
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    category_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tools')
    price_inr = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True, help_text='External image URL (e.g., Unsplash)')
    tags = models.CharField(max_length=255, blank=True, help_text='Comma-separated tags')
    is_featured = models.BooleanField(default=False)
    is_gift = models.BooleanField(default=False)
    is_kit = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} (₹{self.price_inr})'


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    SHIPPING_STATUS_CHOICES = [
        ('Not Shipped', 'Not Shipped'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    shipping_status = models.CharField(max_length=20, choices=SHIPPING_STATUS_CHOICES, default='Not Shipped')
    payment_method = models.CharField(max_length=20, default='COD')
    shipping_name = models.CharField(max_length=200)
    shipping_phone = models.CharField(max_length=20)
    shipping_address_line1 = models.CharField(max_length=255)
    shipping_address_line2 = models.CharField(max_length=255, blank=True)
    shipping_city = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_pincode = models.CharField(max_length=10)
    subtotal_amount = models.PositiveIntegerField(default=0)
    discount_amount = models.PositiveIntegerField(default=0)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'Order #{self.id} - {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()

    def line_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('beginner_setup', 'Full Balcony/Terrace Gardening Setup (Beginners)'),
        ('kit_support', 'Kit Setup Support (Existing Customers)'),
        ('corporate_gifting', 'Corporate Gifting Consultation'),
        ('custom', 'Custom Garden Project'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('contacted', 'Contacted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    budget = models.CharField(max_length=20, blank=True)
    area_size = models.CharField(max_length=20, blank=True)
    preferred_date = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.get_service_type_display()}'


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(max_length=20, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Amount')])
    discount_value = models.PositiveIntegerField(help_text='Percentage (0-100) or Fixed Amount in INR')
    min_purchase_amount = models.PositiveIntegerField(default=0, help_text='Minimum cart value in INR')
    max_discount = models.PositiveIntegerField(null=True, blank=True, help_text='Maximum discount for percentage type')
    usage_limit = models.PositiveIntegerField(null=True, blank=True, help_text='Total usage limit')
    usage_count = models.PositiveIntegerField(default=0)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code} - {self.discount_value}{"%" if self.discount_type == "percentage" else "₹"}'

    def is_valid(self):
        from django.utils import timezone
        now = timezone.now()
        if not self.is_active:
            return False, "Coupon is not active"
        if self.usage_limit and self.usage_count >= self.usage_limit:
            return False, "Coupon usage limit reached"
        if now < self.valid_from:
            return False, "Coupon is not yet valid"
        if now > self.valid_until:
            return False, "Coupon has expired"
        return True, "Valid"

    def calculate_discount(self, cart_total):
        if self.discount_type == 'percentage':
            discount = int(cart_total * self.discount_value / 100)
            if self.max_discount:
                discount = min(discount, self.max_discount)
        else:
            discount = self.discount_value
        return min(discount, cart_total)


class ServicePlan(models.Model):
    """Comprehensive service plans for all categories"""
    PLAN_CATEGORY = [
        ('residential', 'Residential Solutions'),
        ('corporate', 'Corporate Solutions'),
        ('institutional', 'Institutional & Government'),
        ('maintenance', 'Maintenance Plans'),
        ('digital', 'Digital Services'),
        ('workshop', 'Workshops & Events'),
        ('combo', 'Combination Packages'),
        ('custom', 'Custom Solutions'),
    ]
    
    plan_code = models.CharField(max_length=20, unique=True, help_text='e.g., A1, C2, M3')
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300, blank=True)
    category = models.CharField(max_length=20, choices=PLAN_CATEGORY)
    price_inr = models.PositiveIntegerField()
    price_max_inr = models.PositiveIntegerField(null=True, blank=True, help_text='For price ranges')
    space_coverage = models.CharField(max_length=100, blank=True)
    setup_time = models.CharField(max_length=100, blank=True)
    warranty = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    includes_json = models.JSONField(default=list, help_text='List of included items with specifications')
    suitable_plants = models.TextField(blank=True)
    ideal_for = models.TextField(blank=True)
    features = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'display_order', 'price_inr']

    def __str__(self):
        if self.price_max_inr:
            return f'{self.plan_code}: {self.name} (₹{self.price_inr:,} - ₹{self.price_max_inr:,})'
        return f'{self.plan_code}: {self.name} (₹{self.price_inr:,})'


class MaintenancePlan(models.Model):
    """Recurring maintenance service plans"""
    BILLING_PERIOD = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annual', 'Annual'),
    ]
    
    plan_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    billing_period = models.CharField(max_length=20, choices=BILLING_PERIOD)
    price_inr = models.PositiveIntegerField()
    savings_percentage = models.PositiveIntegerField(default=0)
    services_json = models.JSONField(default=list, help_text='List of services with frequency')
    visit_frequency = models.CharField(max_length=100)
    response_time = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', 'price_inr']

    def __str__(self):
        return f'{self.plan_code}: {self.name} - {self.get_billing_period_display()} (₹{self.price_inr:,})'


class WorkshopEvent(models.Model):
    """Workshops and educational events"""
    EVENT_TYPE = [
        ('hobby', 'Hobby Workshop'),
        ('corporate', 'Corporate Workshop'),
    ]
    
    name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE)
    duration = models.CharField(max_length=100)
    price_per_person = models.PositiveIntegerField()
    min_group_size = models.PositiveIntegerField(default=1)
    max_group_size = models.PositiveIntegerField()
    description = models.TextField()
    includes = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - ₹{self.price_per_person:,}/person'


class ServicePackage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_inr = models.PositiveIntegerField()
    service_duration = models.CharField(max_length=100, help_text='e.g., 1 Day, 2-3 Days, 1 Week')
    includes = models.TextField(help_text='What is included in this package')
    is_active = models.BooleanField(default=True)
    service_type = models.CharField(max_length=50, choices=ServiceRequest.SERVICE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} (₹{self.price_inr})'
