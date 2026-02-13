# AURA FARMING – Gardening E‑commerce (Django)

E‑commerce site for gardening accessories, tools, kits, pots, seeds – built with **Python, Django, SQLite**, and **Bootstrap** (HTML/CSS/JS).

## Setup (in the `aura-farming` folder)

1. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # source venv/bin/activate   # Linux/macOS
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations and create a superuser:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
   On first migrate, sample categories and products are created via a `post_migrate` signal.

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   - Site: http://127.0.0.1:8000/  
   - Admin: http://127.0.0.1:8000/admin/ (use the superuser you created)

## Features

- **Shop:** Categories, product list/detail, search, add to cart, cart page, checkout with Indian address (name, phone, address, city, state, pincode), COD; orders are stored in SQLite.
- **User auth:** Register, login, logout; “My Orders” for logged-in users.
- **Admin (Django admin):** Product and category CRUD, order management (status, shipping status), customer profiles, newsletter subscribers, service requests; product images via `ImageField` (optional).
- **Content:** Home page with brand story, featured tool kits, eco-gifts, garden setup service CTA; service request form for full setup / kit support / corporate gifting.
- **Pricing:** All prices in **INR (₹)**; Indian contact/address placeholders in footer.

## Project structure

- `aura_farming/` – Django project settings and URLs.
- `shop/` – Main app: models (Category, Product, Order, OrderItem, CustomerProfile, ServiceRequest, NewsletterSubscriber), views, URLs, forms, cart (session-based), context processor for cart in templates.
- `templates/` – Base template and `shop` templates (home, product list/detail, cart, checkout, order success, register, login, service request, my orders).
- `static/shop/` – CSS and JS (Bootstrap 5 via CDN; minimal custom CSS/JS).
- `media/` – Product uploads (created when you upload images in admin).
- `db.sqlite3` – SQLite database (created after `migrate`).

## Placing an order

1. Open the site, go to Shop, add products to cart.
2. Go to Cart, then “Proceed to Checkout”.
3. Fill shipping details (Indian address) and choose COD.
4. Click “Place Order” – the order is saved and you are redirected to the order success page. Admins can manage orders under **Admin → Orders**.
