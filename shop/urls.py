from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.product_list, name='product_list'),
    path('shop/category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart_view, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('newsletter/subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('services/request/', views.service_request_view, name='service_request'),
    path('my-orders/', views.my_orders, name='my_orders'),
    # Service Plans
    path('services/', views.services_overview, name='services'),
    path('services/plan/<str:plan_code>/', views.service_plan_detail, name='service_plan_detail'),
    path('services/maintenance/', views.maintenance_plans_view, name='maintenance_plans'),
    path('services/workshops/', views.workshops_view, name='workshops'),
    # About
    path('about/', views.about_view, name='about'),
]
