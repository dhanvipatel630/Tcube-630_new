from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    capital = db.Column(db.String(100))

    # Relationships
    destinations = db.relationship('Destination', backref='state', lazy=True)
    restaurants = db.relationship('Restaurant', backref='state', lazy=True)
    hospitals = db.relationship('Hospital', backref='state', lazy=True)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    rating = db.Column(db.Float, default=0.0)
    category = db.Column(db.String(100))
    entry_fee = db.Column(db.String(100))
    contact = db.Column(db.String(200))
    best_time = db.Column(db.String(200))

    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    rating = db.Column(db.Float, default=0.0)
    cuisine_type = db.Column(db.String(100))
    price_range = db.Column(db.String(50))
    contact = db.Column(db.String(200))
    famous_dishes = db.Column(db.Text)

    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    rating = db.Column(db.Float, default=0.0)
    hospital_type = db.Column(db.String(100))
    specialties = db.Column(db.Text)
    contact = db.Column(db.String(200))
    emergency_services = db.Column(db.Boolean, default=True)
    bed_count = db.Column(db.Integer)

    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)