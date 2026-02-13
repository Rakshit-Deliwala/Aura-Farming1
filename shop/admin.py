from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import Sum, Count
from django.utils import timezone
from .models import (
    Category,
    Product,
    CustomerProfile,
    Order,
    OrderItem,
    NewsletterSubscriber,
    ServiceRequest,
    Coupon,
    ServicePackage,
    ServicePlan,
    MaintenancePlan,
    WorkshopEvent,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'product_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    def product_count(self, obj):
        return obj.product_set.count()
    product_count.short_description = 'Products'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'unit_price', 'line_total')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_thumbnail', 'category', 'category_type', 'price_inr', 'stock', 'is_kit', 'is_gift', 'is_featured', 'created_at')
    list_filter = ('category_type', 'is_kit', 'is_gift', 'is_featured', 'created_at', 'category')
    search_fields = ('name', 'tags', 'description')
    list_editable = ('price_inr', 'stock', 'is_featured')
    list_display_links = ('name', 'admin_thumbnail')
    date_hierarchy = 'created_at'
    list_per_page = 50
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'category_type', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price_inr', 'stock')
        }),
        ('Images & Tags', {
            'fields': ('image', 'tags')
        }),
        ('Product Flags', {
            'fields': ('is_featured', 'is_gift', 'is_kit')
        }),
    )

    def admin_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="" style="max-height:40px; max-width:60px; object-fit:contain;">')
        return '—'
    admin_thumbnail.short_description = 'Image'

    actions = ['mark_as_featured', 'mark_as_not_featured', 'increase_stock']

    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} products marked as featured.')
    mark_as_featured.short_description = 'Mark selected as featured'

    def mark_as_not_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} products removed from featured.')
    mark_as_not_featured.short_description = 'Remove from featured'

    def increase_stock(self, request, queryset):
        for product in queryset:
            product.stock += 10
            product.save()
        self.message_user(request, f'Stock increased by 10 for {queryset.count()} products.')
    increase_stock.short_description = 'Increase stock by 10'


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'state', 'total_orders')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'phone', 'city')
    list_filter = ('state', 'city')

    def total_orders(self, obj):
        return obj.user.order_set.count()
    total_orders.short_description = 'Total Orders'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'shipping_status', 'total_amount', 'payment_method', 'created_at')
    list_filter = ('status', 'shipping_status', 'payment_method', 'created_at')
    search_fields = ('id', 'user__username', 'user__email', 'shipping_phone', 'shipping_name')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at', 'subtotal_amount', 'discount_amount', 'coupon')
    list_editable = ('status', 'shipping_status')
    date_hierarchy = 'created_at'
    list_per_page = 50
    
    fieldsets = (
        ('Order Information', {
            'fields': ('user', 'status', 'shipping_status', 'payment_method', 'created_at')
        }),
        ('Shipping Details', {
            'fields': ('shipping_name', 'shipping_phone', 'shipping_address_line1', 'shipping_address_line2', 
                       'shipping_city', 'shipping_state', 'shipping_pincode')
        }),
        ('Payment Details', {
            'fields': ('subtotal_amount', 'discount_amount', 'coupon', 'total_amount')
        }),
        ('Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )

    actions = ['mark_as_processing', 'mark_as_shipped', 'mark_as_delivered']

    def mark_as_processing(self, request, queryset):
        updated = queryset.update(status='Processing')
        self.message_user(request, f'{updated} orders marked as Processing.')
    mark_as_processing.short_description = 'Mark as Processing'

    def mark_as_shipped(self, request, queryset):
        updated = queryset.update(shipping_status='Shipped')
        self.message_user(request, f'{updated} orders marked as Shipped.')
    mark_as_shipped.short_description = 'Mark as Shipped'

    def mark_as_delivered(self, request, queryset):
        updated = queryset.update(shipping_status='Delivered', status='Completed')
        self.message_user(request, f'{updated} orders marked as Delivered & Completed.')
    mark_as_delivered.short_description = 'Mark as Delivered'


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    date_hierarchy = 'created_at'


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'city', 'service_type', 'budget', 'area_size', 'status', 'created_at')
    list_filter = ('service_type', 'status', 'budget', 'area_size', 'city', 'created_at')
    search_fields = ('name', 'email', 'phone', 'city', 'address')
    list_editable = ('status',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone', 'city', 'address')
        }),
        ('Service Details', {
            'fields': ('service_type', 'budget', 'area_size', 'preferred_date', 'message', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'usage_count', 'usage_limit', 'valid_from', 'valid_until', 'is_active')
    list_filter = ('discount_type', 'is_active', 'valid_from', 'valid_until')
    search_fields = ('code',)
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Coupon Details', {
            'fields': ('code', 'discount_type', 'discount_value')
        }),
        ('Restrictions', {
            'fields': ('min_purchase_amount', 'max_discount', 'usage_limit', 'usage_count')
        }),
        ('Validity', {
            'fields': ('valid_from', 'valid_until', 'is_active')
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.code = obj.code.upper()
        super().save_model(request, obj, form, change)


@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'price_inr', 'service_duration', 'is_active')
    list_filter = ('service_type', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('is_active', 'price_inr')


@admin.register(ServicePlan)
class ServicePlanAdmin(admin.ModelAdmin):
    list_display = ('plan_code', 'name', 'category', 'price_display', 'space_coverage', 'is_featured', 'is_active', 'display_order')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('plan_code', 'name', 'tagline', 'description')
    list_editable = ('is_featured', 'is_active', 'display_order')
    ordering = ('category', 'display_order')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('plan_code', 'name', 'tagline', 'category', 'description')
        }),
        ('Pricing & Coverage', {
            'fields': ('price_inr', 'price_max_inr', 'space_coverage', 'setup_time', 'warranty')
        }),
        ('Details', {
            'fields': ('includes_json', 'suitable_plants', 'ideal_for', 'features')
        }),
        ('Settings', {
            'fields': ('is_active', 'is_featured', 'display_order')
        }),
    )
    
    def price_display(self, obj):
        if obj.price_max_inr:
            return f'₹{obj.price_inr:,} - ₹{obj.price_max_inr:,}'
        return f'₹{obj.price_inr:,}'
    price_display.short_description = 'Price'


@admin.register(MaintenancePlan)
class MaintenancePlanAdmin(admin.ModelAdmin):
    list_display = ('plan_code', 'name', 'billing_period', 'price_inr', 'savings_percentage', 'visit_frequency', 'is_active', 'display_order')
    list_filter = ('billing_period', 'is_active')
    search_fields = ('plan_code', 'name', 'description')
    list_editable = ('is_active', 'display_order')
    ordering = ('display_order',)
    
    fieldsets = (
        ('Plan Information', {
            'fields': ('plan_code', 'name', 'description', 'billing_period')
        }),
        ('Pricing', {
            'fields': ('price_inr', 'savings_percentage')
        }),
        ('Service Details', {
            'fields': ('services_json', 'visit_frequency', 'response_time')
        }),
        ('Settings', {
            'fields': ('is_active', 'display_order')
        }),
    )


@admin.register(WorkshopEvent)
class WorkshopEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_type', 'duration', 'price_per_person', 'group_size_range', 'is_active')
    list_filter = ('event_type', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    
    fieldsets = (
        ('Event Information', {
            'fields': ('name', 'event_type', 'description')
        }),
        ('Pricing & Duration', {
            'fields': ('duration', 'price_per_person', 'min_group_size', 'max_group_size')
        }),
        ('Details', {
            'fields': ('includes',)
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )
    
    def group_size_range(self, obj):
        return f'{obj.min_group_size}-{obj.max_group_size} participants'
    group_size_range.short_description = 'Group Size'


# Custom Admin Site Title
admin.site.site_header = 'AURA FARMING Admin'
admin.site.site_title = 'AURA FARMING Admin Portal'
admin.site.index_title = 'Welcome to AURA FARMING Admin'
