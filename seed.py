from app import create_app, db, Product

app = create_app()

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()
    
    # Insert new data
    products = [
        Product(id=1, name='Espresso Coffee', type='coffee', sizes={'small': 15.00, 'medium': 30.00, 'large': 50.00}),
        Product(id=2, name='Latte', type='coffee', sizes={'small': 15.00, 'medium': 30.00, 'large': 50.00}),
        Product(id=3, name='Cold Brew', type='coffee', sizes={'small': 15.00, 'medium': 30.00, 'large': 50.00}),
        Product(id=4, name='Black Coffee', type='coffee', sizes={'small': 15.00, 'medium': 30.00, 'large': 50.00}),
        Product(id=5, name='Cappuccino', type='coffee', sizes={'small': 15.00, 'medium': 30.00, 'large': 50.00}),
        Product(id=6, name='Matcha Latte', type='coffee', sizes={'small': 15.00, 'medium': 30.00, 'large': 50.00}),
        Product(id=7, name='Ice Cream Waffles', type='dessert', sizes={'regular': 250.00}),
        Product(id=8, name='Cheesecake', type='dessert', sizes={'regular': 250.00}),
    ]
    
    db.session.bulk_save_objects(products)
    db.session.commit()
