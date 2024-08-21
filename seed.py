from app import db
from models import Coffee, Dessert

def seed_data():
    coffees = [
        Coffee(name='Espresso', price_s=15.00, price_m=30.00, price_l=50.00),
        Coffee(name='Cold Brew', price_s=15.00, price_m=30.00, price_l=50.00),
        Coffee(name='Matcha', price_s=15.00, price_m=30.00, price_l=50.00),
        Coffee(name='Latte (Caramel or Vanilla)', price_s=15.00, price_m=30.00, price_l=50.00),
        Coffee(name='Mocha', price_s=15.00, price_m=30.00, price_l=50.00),
        Coffee(name='Black Coffee', price_s=15.00, price_m=30.00, price_l=50.00),
        Coffee(name='Cappuccino', price_s=15.00, price_m=30.00, price_l=50.00)
    ]

    desserts = [
        Dessert(name='Ice Cream Waffles', price=50.00),
        Dessert(name='Cheesecake', price=50.00),
        Dessert(name='Caramel Cupcake', price=50.00),
        Dessert(name='Strawberry Cupcake', price=50.00),
        Dessert(name='White Cream Cupcake', price=50.00),
        Dessert(name='Lotus Biscuits', price=50.00)
    ]

    db.session.bulk_save_objects(coffees + desserts)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_data()
