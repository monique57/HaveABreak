from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Sample data for products
    products = [
        {'id': 1, 'name': 'Espresso Coffee', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 2, 'name': 'Latte', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        {'id': 3, 'name': 'Cold Brew', 'type': 'coffee', 'sizes': {'small': 15.00, 'medium': 30.00, 'large': 50.00}},
        # Add more products as needed
    ]
    return render_template('index.html', products=products)


@app.route('/add-to-cart/<int:product_id>/<product_type>/<size>')
def add_to_cart(product_id, product_type, size):
    cart = session.get('cart', {})
    
    item_key = f'{product_type}_{product_id}_{size}'
    
    if item_key in cart:
        cart[item_key]['quantity'] += 1
    else:
        cart[item_key] = {
            'product_id': product_id,
            'product_type': product_type,
            'size': size,
            'quantity': 1,
            'price': 15.00 if size == 'small' else 30.00 if size == 'medium' else 50.00
        }
    
    session['cart'] = cart
    session.modified = True  # Ensure the session is updated
    return redirect(url_for('index'))


@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Process the order here
        customer_name = request.form.get('name')
        customer_email = request.form.get('email')
        shipping_address = request.form.get('address')

        # Example: Retrieve cart items and calculate total price
        cart = session.get('cart', {})
        total_price = sum(item['price'] * item['quantity'] for item in cart.values())

        # Here you would typically save the order to a database and process payment
        # For now, we’ll just clear the cart and redirect to a confirmation page
        session.pop('cart', None)

        return redirect(url_for('order_confirmation', name=customer_name, total_price=total_price))

    return render_template('checkout.html')

@app.route('/order-confirmation')
def order_confirmation():
    name = request.args.get('name')
    total_price = request.args.get('total_price')
    return render_template('order_confirmation.html', name=name, total_price=total_price)