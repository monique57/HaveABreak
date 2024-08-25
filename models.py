from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coffee(db.Model):
    __tablename__ = 'coffees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_s = db.Column(db.Float, nullable=False)  # Small price
    price_m = db.Column(db.Float, nullable=False)  # Medium price
    price_l = db.Column(db.Float, nullable=False)  # Large price

    def __repr__(self):
        return f'<Coffee {self.name}>'

class Dessert(db.Model):
    __tablename__ = 'desserts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Dessert {self.name}>'  

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    sizes = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

