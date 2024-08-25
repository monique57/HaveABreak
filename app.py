from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

load_dotenv()  # Load environment variables from .env

# Initialize SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')

@app.route('/')
def index():
    products = [
        {'id': 1, 'name': 'Espresso Coffee', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 2, 'name': 'Latte', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 3, 'name': 'Cold Brew', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 4, 'name': 'Black Coffee', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 5, 'name': 'Cappuccino', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 6, 'name': 'Matcha Latte', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 7, 'name': 'Ice Cream Waffles', 'type': 'dessert', 'sizes': {'regular': 250.00}},
        {'id': 8, 'name': 'Cheesecake', 'type': 'dessert', 'sizes': {'regular': 250.00}},
    ]
    return render_template('index.html', products=products)

@app.route('/add-to-cart/<int:product_id>/<size>')
def add_to_cart(product_id, size):
    cart = session.get('cart', {})

    # Fetch the product by ID
    products = [
        {'id': 1, 'name': 'Espresso Coffee', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 2, 'name': 'Latte', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 3, 'name': 'Cold Brew', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 4, 'name': 'Black Coffee', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 5, 'name': 'Cappuccino', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 6, 'name': 'Matcha Latte', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 7, 'name': 'Ice Cream Waffles', 'type': 'dessert', 'sizes': {'regular': 250.00}},
        {'id': 8, 'name': 'Cheesecake', 'type': 'dessert', 'sizes': {'regular': 250.00}},
    ]

    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return redirect(url_for('index'))

    item_key = f'{product["type"]}_{product_id}_{size}'
    price = product['sizes'][size]

    if item_key in cart:
        cart[item_key]['quantity'] += 1
    else:
        cart[item_key] = {
            'product_name': product['name'],
            'product_type': product['type'],
            'size': size,
            'quantity': 1,
            'price': price
        }
    
    session['cart'] = cart
    session.modified = True
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        customer_name = request.form.get('name')
        customer_email = request.form.get('email')
        shipping_address = request.form.get('address')

        cart = session.get('cart', {})
        total_price = sum(item['price'] * item['quantity'] for item in cart.values())

        session.pop('cart', None)

        return redirect(url_for('order_confirmation', name=customer_name, total_price=f"{total_price:.2f} TRY"))

    cart = session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('checkout.html', cart=cart, total_price=total_price)

@app.route('/order-confirmation')
def order_confirmation():
    name = request.args.get('name')
    total_price = request.args.get('total_price')
    return render_template('order_confirmation.html', name=name, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)
