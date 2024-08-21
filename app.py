from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Your code for displaying coffee and dessert items
    return render_template('index.html')

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
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_price=total_price)
