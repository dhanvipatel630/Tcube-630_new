from flask import Flask, render_template, request
from models import db, State, Destination, Restaurant, Hospital
import os
from pathlib import Path

# Create Flask ap
app = Flask(__name__)

# Fix paths to prevent database errors
BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / 'instance'
INSTANCE_DIR.mkdir(exist_ok=True)

# Configuration
app.config['SECRET_KEY'] = 'tcube-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{INSTANCE_DIR / "tcube.db"}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

@app.route('/')
def index():
    search = request.args.get('search', '')

    if search:
        states = State.query.filter(
            db.or_(
                State.name.contains(search),
                State.description.contains(search)
            )
        ).all()
    else:
        states = State.query.all()

    return render_template('index.html', states=states, search=search)

@app.route('/state/<int:state_id>')
def state_detail(state_id):
    state = State.query.get_or_404(state_id)
    return render_template('state_detail.html', state=state)

@app.route('/state/<int:state_id>/travel')
def travel(state_id):
    state = State.query.get_or_404(state_id)
    search = request.args.get('search', '')
    category = request.args.get('category', '')
    sort_by = request.args.get('sort', 'rating')

    query = Destination.query.filter_by(state_id=state_id)

    if search:
        query = query.filter(
            db.or_(
                Destination.name.contains(search),
                Destination.location.contains(search)
            )
        )

    if category:
        query = query.filter_by(category=category)

    if sort_by == 'name':
        destinations = query.order_by(Destination.name).all()
    else:
        destinations = query.order_by(Destination.rating.desc()).all()

    categories = db.session.query(Destination.category.distinct()).filter_by(state_id=state_id).all()
    categories = [cat[0] for cat in categories if cat[0]]

    return render_template('travel.html', 
                         state=state, 
                         destinations=destinations,
                         categories=categories,
                         current_search=search,
                         current_category=category,
                         current_sort=sort_by)

@app.route('/state/<int:state_id>/taste')
def taste(state_id):
    state = State.query.get_or_404(state_id)
    search = request.args.get('search', '')
    cuisine = request.args.get('cuisine', '')
    sort_by = request.args.get('sort', 'rating')

    query = Restaurant.query.filter_by(state_id=state_id)

    if search:
        query = query.filter(
            db.or_(
                Restaurant.name.contains(search),
                Restaurant.location.contains(search)
            )
        )

    if cuisine:
        query = query.filter_by(cuisine_type=cuisine)

    if sort_by == 'name':
        restaurants = query.order_by(Restaurant.name).all()
    else:
        restaurants = query.order_by(Restaurant.rating.desc()).all()

    cuisines = db.session.query(Restaurant.cuisine_type.distinct()).filter_by(state_id=state_id).all()
    cuisines = [cuisine[0] for cuisine in cuisines if cuisine[0]]

    return render_template('taste.html', 
                         state=state, 
                         restaurants=restaurants,
                         cuisines=cuisines,
                         current_search=search,
                         current_cuisine=cuisine,
                         current_sort=sort_by)

@app.route('/state/<int:state_id>/treatment')
def treatment(state_id):
    state = State.query.get_or_404(state_id)
    search = request.args.get('search', '')
    hospital_type = request.args.get('type', '')
    emergency_only = request.args.get('emergency') == 'on'
    sort_by = request.args.get('sort', 'rating')

    query = Hospital.query.filter_by(state_id=state_id)

    if search:
        query = query.filter(
            db.or_(
                Hospital.name.contains(search),
                Hospital.location.contains(search)
            )
        )

    if hospital_type:
        query = query.filter_by(hospital_type=hospital_type)

    if emergency_only:
        query = query.filter_by(emergency_services=True)

    if sort_by == 'name':
        hospitals = query.order_by(Hospital.name).all()
    else:
        hospitals = query.order_by(Hospital.rating.desc()).all()

    types = db.session.query(Hospital.hospital_type.distinct()).filter_by(state_id=state_id).all()
    types = [t[0] for t in types if t[0]]

    return render_template('treatment.html', 
                         state=state, 
                         hospitals=hospitals,
                         hospital_types=types,
                         current_search=search,
                         current_type=hospital_type,
                         current_emergency=emergency_only,
                         current_sort=sort_by)

# Simple error handling without template files
@app.errorhandler(404)
def not_found_error(error):
    return '''
    <html>
    <head><title>Page Not Found - T-Cube</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px; background: linear-gradient(135deg, #667eea, #764ba2); color: white;">
        <h1>🔍 404 - Page Not Found</h1>
        <p>The page you're looking for doesn't exist.</p>
        <a href="/" style="color: white; background: rgba(255,255,255,0.2); padding: 10px 20px; text-decoration: none; border-radius: 25px;">Go Home</a>
    </body>
    </html>
    ''', 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return '''
    <html>
    <head><title>Server Error - T-Cube</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px; background: linear-gradient(135deg, #f093fb, #f5576c); color: white;">
        <h1>⚠️ 500 - Server Error</h1>
        <p>Something went wrong. We're working to fix it!</p>
        <a href="/" style="color: white; background: rgba(255,255,255,0.2); padding: 10px 20px; text-decoration: none; border-radius: 25px;">Go Home</a>
    </body>
    </html>
    ''', 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)