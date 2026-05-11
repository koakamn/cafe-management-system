# Cafe

A web app for a cafe built with Django. Customers can browse the menu, filter by category, add items to a session-based cart, and place orders. Includes user registration and login.

## Tech stack

- Django 6.0
- SQLite
- Bootstrap 5.3
- Pillow (for image uploads)

## Project structure

The project is split into four Django apps:

- **core** — static pages: home, about, contact
- **menu** — product catalog with categories and detail pages
- **orders** — cart (session-based), checkout, order history
- **users** — registration form

Templates extend a shared `base.html` with a Bootstrap navbar and footer. The cart counter in the navbar is powered by a context processor (`orders.context_processors.cart`).

## Getting started

```bash
# create a virtual environment
python -m venv venv
venv\Scripts\activate        # on Windows
# source venv/bin/activate   # on macOS/Linux

# install dependencies
pip install django pillow

# run migrations and create an admin user
python manage.py migrate
python manage.py createsuperuser

# start the dev server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. Add categories and products through the admin panel at `/admin/`.

## Routes

| Path | What it does |
|------|-------------|
| `/` | Home page |
| `/about/` | About page |
| `/contact/` | Contact page |
| `/menu/` | Menu list (supports `?category=<id>` filtering) |
| `/menu/<id>/` | Product detail |
| `/cart/` | View cart |
| `/cart/add/<id>/` | Add product to cart |
| `/cart/remove/<id>/` | Remove product from cart |
| `/cart/update/<id>/<qty>/` | Update quantity |
| `/cart/checkout/` | Checkout (login required) |
| `/cart/my-orders/` | Order history (login required) |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/users/register/` | Registration |
| `/admin/` | Django admin |

## Models

**Category** — just a name.

**Product** — belongs to a category; has name, description, price, image, and an `available` flag.

**Order** — stores customer name, phone, address, a link to the user, and a timestamp.

**OrderItem** — links an order to a product with price and quantity captured at the time of purchase.

## How the cart works

The cart lives entirely in the Django session (`request.session['cart']`). It stores a dict mapping product IDs to quantities. No database writes happen until the user goes through checkout. The `Cart` class in `orders/cart.py` handles add/remove/update and exposes iteration and total price calculation.

