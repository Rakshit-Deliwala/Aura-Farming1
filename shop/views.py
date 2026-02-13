from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db import transaction
from django.urls import resolve

from .models import Product, Category, Order, OrderItem, NewsletterSubscriber, CustomerProfile, ServicePlan, MaintenancePlan, WorkshopEvent
from .forms import RegistrationForm, CheckoutForm, ServiceRequestForm
from .cart import add_to_cart, remove_from_cart, get_cart_items, get_cart_totals, clear_cart


def home(request):
    featured_kits = Product.objects.filter(is_kit=True, is_featured=True)[:4]
    eco_gifts = Product.objects.filter(is_gift=True, is_featured=True)[:4]
    tools = Product.objects.filter(category_type='tools')[:4]
    return render(request, 'shop/home.html', {
        'featured_kits': featured_kits,
        'eco_gifts': eco_gifts,
        'tools': tools,
    })


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)
    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


def add_to_cart_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    add_to_cart(request, product.id, 1)
    messages.success(request, f'"{product.name}" added to your cart.')
    return redirect('shop:cart')


def remove_from_cart_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    remove_from_cart(request, product.id)
    messages.info(request, f'"{product.name}" removed from your cart.')
    return redirect('shop:cart')


def cart_view(request):
    items = get_cart_items(request)
    totals = get_cart_totals(request)
    return render(request, 'shop/cart.html', {
        'items': items,
        'total_amount': totals['total_amount'],
        'total_quantity': totals['total_quantity'],
    })


@transaction.atomic
def checkout(request):
    items = get_cart_items(request)
    totals = get_cart_totals(request)
    if not items:
        messages.warning(request, 'Your cart is empty. Please add products before checkout.')
        return redirect('shop:product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                status='Pending',
                shipping_status='Not Shipped',
                payment_method=data['payment_method'],
                shipping_name=data['name'],
                shipping_phone=data['phone'],
                shipping_address_line1=data['address_line1'],
                shipping_address_line2=data.get('address_line2') or '',
                shipping_city=data['city'],
                shipping_state=data['state'],
                shipping_pincode=data['pincode'],
                subtotal_amount=totals['total_amount'],
                discount_amount=0,
                total_amount=totals['total_amount'],
            )
            for item in items:
                product = item['product']
                qty = item['quantity']
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=qty,
                    unit_price=product.price_inr,
                )
                if product.stock >= qty:
                    product.stock -= qty
                    product.save()
            if request.user.is_authenticated:
                try:
                    profile = request.user.customerprofile
                    profile.phone = data.get('phone') or profile.phone
                    profile.address_line1 = data.get('address_line1') or profile.address_line1
                    profile.address_line2 = data.get('address_line2') or profile.address_line2
                    profile.city = data.get('city') or profile.city
                    profile.state = data.get('state') or profile.state
                    profile.pincode = data.get('pincode') or profile.pincode
                    profile.save()
                except CustomerProfile.DoesNotExist:
                    CustomerProfile.objects.create(
                        user=request.user,
                        phone=data.get('phone', ''),
                        address_line1=data.get('address_line1', ''),
                        address_line2=data.get('address_line2', ''),
                        city=data.get('city', ''),
                        state=data.get('state', ''),
                        pincode=data.get('pincode', '')
                    )
            clear_cart(request)
            messages.success(request, f'Your order #{order.id} has been placed successfully! We will contact you for COD confirmation.')
            return redirect('shop:order_success', order_id=order.id)
    else:
        initial = {}
        if request.user.is_authenticated:
            user = request.user
            initial['name'] = user.get_full_name() or user.username
            initial['phone'] = ''
            try:
                profile = user.customerprofile
                initial.setdefault('phone', profile.phone or '')
                initial.setdefault('address_line1', profile.address_line1 or '')
                initial.setdefault('address_line2', profile.address_line2 or '')
                initial.setdefault('city', profile.city or 'Bengaluru')
                initial.setdefault('state', profile.state or 'Karnataka')
                initial.setdefault('pincode', profile.pincode or '560001')
            except CustomerProfile.DoesNotExist:
                pass
        form = CheckoutForm(initial=initial)

    return render(request, 'shop/checkout.html', {
        'form': form,
        'items': items,
        'total_amount': totals['total_amount'],
    })


def order_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.user is not None:
        if not request.user.is_authenticated or (request.user != order.user and not request.user.is_staff):
            messages.error(request, 'You do not have permission to view this order.')
            return redirect('shop:home')
    return render(request, 'shop/order_success.html', {'order': order})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            CustomerProfile.objects.get_or_create(user=user)
            messages.success(request, 'Registration successful. You can now sign in.')
            return redirect('shop:login')
    else:
        form = RegistrationForm()
    return render(request, 'shop/register.html', {'form': form})


def login_view(request):
    next_url = request.GET.get('next') or request.POST.get('next') or ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Signed in successfully.')
            if next_url and next_url.startswith('/') and not next_url.startswith('//'):
                try:
                    resolve(next_url)
                    return redirect(next_url)
                except Exception:
                    pass
            return redirect('shop:home')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'shop/login.html', {'next': next_url})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('shop:home')


def subscribe_newsletter(request):
    email = request.POST.get('email')
    if email:
        NewsletterSubscriber.objects.get_or_create(email=email)
        messages.success(request, 'Thank you for subscribing to AURA FARMING updates!')
    return redirect('shop:home')


def service_request_view(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Our team will contact you within 24 hours for your gardening setup.')
            return redirect('shop:home')
    else:
        form = ServiceRequestForm()
    return render(request, 'shop/service_request.html', {'form': form})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/my_orders.html', {'orders': orders})


def services_overview(request):
    """Main services page with all categories"""
    residential = ServicePlan.objects.filter(category='residential', is_active=True)
    corporate = ServicePlan.objects.filter(category='corporate', is_active=True)
    institutional = ServicePlan.objects.filter(category='institutional', is_active=True)
    maintenance_plans = MaintenancePlan.objects.filter(is_active=True)
    workshops = WorkshopEvent.objects.filter(is_active=True)
    
    context = {
        'residential': residential,
        'corporate': corporate,
        'institutional': institutional,
        'maintenance_plans': maintenance_plans,
        'workshops': workshops,
    }
    return render(request, 'shop/services_overview.html', context)


def service_plan_detail(request, plan_code):
    """Individual service plan detail page"""
    plan = get_object_or_404(ServicePlan, plan_code=plan_code, is_active=True)
    related_plans = ServicePlan.objects.filter(
        category=plan.category, is_active=True
    ).exclude(plan_code=plan_code)[:3]
    
    context = {
        'plan': plan,
        'related_plans': related_plans,
    }
    return render(request, 'shop/service_plan_detail.html', context)


def maintenance_plans_view(request):
    """Maintenance plans comparison page"""
    basic_plans = MaintenancePlan.objects.filter(name='Basic Care', is_active=True)
    comprehensive_plans = MaintenancePlan.objects.filter(name='Comprehensive Care', is_active=True)
    corporate_plans = MaintenancePlan.objects.filter(name='Corporate Care', is_active=True)
    
    # Add workshop events for combined page
    hobby_workshops = WorkshopEvent.objects.filter(event_type='hobby', is_active=True)[:4]  # Limit to 4 for display
    
    context = {
        'basic_plans': basic_plans,
        'comprehensive_plans': comprehensive_plans,
        'corporate_plans': corporate_plans,
        'hobby_workshops': hobby_workshops,
    }
    return render(request, 'shop/maintenance_plans.html', context)


def workshops_view(request):
    """Workshops and events listing"""
    hobby_workshops = WorkshopEvent.objects.filter(event_type='hobby', is_active=True)
    corporate_workshops = WorkshopEvent.objects.filter(event_type='corporate', is_active=True)
    
    context = {
        'hobby_workshops': hobby_workshops,
        'corporate_workshops': corporate_workshops,
    }
    return render(request, 'shop/workshops.html', context)


def about_view(request):
    """About Us page"""
    return render(request, 'shop/about.html')

