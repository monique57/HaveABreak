from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coffee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_s = db.Column(db.Float, nullable=False)
    price_m = db.Column(db.Float, nullable=False)
    price_l = db.Column(db.Float, nullable=False)

class Dessert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
