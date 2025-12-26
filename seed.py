from flask import Flask
from models import db, State, Destination, Restaurant, Hospital
from pathlib import Path

def create_app():
    app = Flask(__name__)

    # Fix paths to prevent database errors
    BASE_DIR = Path(__file__).resolve().parent
    INSTANCE_DIR = BASE_DIR / 'instance'
    INSTANCE_DIR.mkdir(exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{INSTANCE_DIR / "tcube.db"}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def seed_data():
    app = create_app()

    with app.app_context():
        print("Dropping existing tables...")
        db.drop_all()

        print("Creating new tables...")
        db.create_all()

        # States data
        states_data = [
            {'name': 'Maharashtra', 'description': 'Financial capital with Bollywood, beaches and heritage sites', 'image_url': 'https://images.unsplash.com/photo-1586880244386-8b3e34c8382c?w=600', 'capital': 'Mumbai'},
            {'name': 'Gujarat', 'description': 'Land of business, culture and the magnificent Statue of Unity', 'image_url': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=600', 'capital': 'Gandhinagar'},
            {'name': 'Karnataka', 'description': 'Silicon Valley of India with royal heritage and gardens', 'image_url': 'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=600', 'capital': 'Bengaluru'},
            {'name': 'Tamil Nadu', 'description': 'Land of ancient temples, classical arts and rich culture', 'image_url': 'https://images.unsplash.com/photo-1582563271933-0e5c7bbad5d5?w=600', 'capital': 'Chennai'},
            {'name': 'Rajasthan', 'description': 'Royal state with magnificent palaces, forts and desert landscapes', 'image_url': 'https://images.unsplash.com/photo-1477587458883-47145ed94245?w=600', 'capital': 'Jaipur'},
            {'name': 'Kerala', 'description': 'Gods Own Country with backwaters, spices and scenic beauty', 'image_url': 'https://images.unsplash.com/photo-1520637836862-4d197d17c43a?w=600', 'capital': 'Thiruvananthapuram'},
            {'name': 'Uttar Pradesh', 'description': 'Home to the iconic Taj Mahal and rich Mughal heritage', 'image_url': 'https://images.unsplash.com/photo-1564507592333-c60657eea523?w=600', 'capital': 'Lucknow'},
            {'name': 'West Bengal', 'description': 'Cultural capital known for art, literature and sweets', 'image_url': 'https://images.unsplash.com/photo-1590736969955-71cc94901144?w=600', 'capital': 'Kolkata'},
            {'name': 'Punjab', 'description': 'Land of five rivers, Golden Temple and vibrant culture', 'image_url': 'https://images.unsplash.com/photo-1578021046445-3b7c8bdd16db?w=600', 'capital': 'Chandigarh'},
            {'name': 'Goa', 'description': 'Beach paradise with Portuguese heritage and vibrant nightlife', 'image_url': 'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=600', 'capital': 'Panaji'},
            {'name': 'Delhi', 'description': 'National capital with rich history and modern infrastructure', 'image_url': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=600', 'capital': 'New Delhi'},
            {'name': 'Andhra Pradesh', 'description': 'Known for spicy cuisine, ancient temples and rich traditions', 'image_url': 'https://images.unsplash.com/photo-1526901382726-2c12d31c6e5c?w=600', 'capital': 'Amaravati'}
        ]

        # Create states
        print("Creating states...")
        states = {}
        for state_data in states_data:
            state = State(**state_data)
            db.session.add(state)
            db.session.commit()
            states[state.name] = state
            print(f"  ✓ {state.name}")

        # Create destinations with realistic data
        print("Creating destinations...")
        destinations_data = []

        # Add detailed destinations for major states
        major_destinations = {
            'Maharashtra': [
                {'name': 'Gateway of India', 'location': 'Mumbai', 'description': 'Iconic arch monument overlooking the Arabian Sea, built to commemorate the visit of King George V', 'image_url': 'https://images.unsplash.com/photo-1595658658481-d53d3f999875?w=400', 'rating': 4.5, 'category': 'Monument', 'entry_fee': 'Free', 'contact': '+91-22-22625585', 'best_time': 'Oct-Mar'},
                {'name': 'Ajanta Caves', 'location': 'Aurangabad', 'description': 'Ancient Buddhist rock-cut caves with exquisite paintings and sculptures', 'image_url': 'https://images.unsplash.com/photo-1578068536253-45a43e7ccdfe?w=400', 'rating': 4.8, 'category': 'Heritage', 'entry_fee': '₹40', 'contact': '+91-240-2336142', 'best_time': 'Oct-Mar'},
                {'name': 'Marine Drive', 'location': 'Mumbai', 'description': 'Beautiful 3.6 km coastal promenade known as Queens Necklace', 'image_url': 'https://images.unsplash.com/photo-1586880244386-8b3e34c8382c?w=400', 'rating': 4.3, 'category': 'Waterfront', 'entry_fee': 'Free', 'contact': 'N/A', 'best_time': 'Oct-Mar'},
                {'name': 'Lonavala Hill Station', 'location': 'Pune District', 'description': 'Popular hill station with lush valleys, waterfalls and pleasant weather', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400', 'rating': 4.2, 'category': 'Hill Station', 'entry_fee': 'Free', 'contact': '+91-2114-273314', 'best_time': 'Jun-Sep'},
                {'name': 'Elephanta Caves', 'location': 'Mumbai Harbor', 'description': 'Ancient cave temples dedicated to Lord Shiva on Elephanta Island', 'image_url': 'https://images.unsplash.com/photo-1578068536253-45a43e7ccdfe?w=400', 'rating': 4.1, 'category': 'Heritage', 'entry_fee': '₹40', 'contact': '+91-22-22844040', 'best_time': 'Oct-Mar'},
                {'name': 'Shirdi Sai Temple', 'location': 'Ahmednagar', 'description': 'Sacred pilgrimage site of Sai Baba attracting millions of devotees', 'image_url': 'https://images.unsplash.com/photo-1578021046445-3b7c8bdd16db?w=400', 'rating': 4.6, 'category': 'Temple', 'entry_fee': 'Free', 'contact': '+91-2423-258500', 'best_time': 'Oct-Mar'}
            ],
            'Gujarat': [
                {'name': 'Statue of Unity', 'location': 'Kevadiya', 'description': 'Worlds tallest statue at 182m dedicated to Sardar Vallabhbhai Patel', 'image_url': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', 'rating': 4.7, 'category': 'Monument', 'entry_fee': '₹120', 'contact': '+91-2697-276276', 'best_time': 'Oct-Mar'},
                {'name': 'Rann of Kutch', 'location': 'Kutch District', 'description': 'Spectacular white salt desert with unique landscape and culture', 'image_url': 'https://images.unsplash.com/photo-1477587458883-47145ed94245?w=400', 'rating': 4.8, 'category': 'Desert', 'entry_fee': 'Free', 'contact': '+91-2832-255104', 'best_time': 'Nov-Feb'},
                {'name': 'Sabarmati Ashram', 'location': 'Ahmedabad', 'description': 'Mahatma Gandhis former residence and museum of his life', 'image_url': 'https://images.unsplash.com/photo-1578021046445-3b7c8bdd16db?w=400', 'rating': 4.5, 'category': 'Museum', 'entry_fee': 'Free', 'contact': '+91-79-27570956', 'best_time': 'Oct-Mar'},
                {'name': 'Dwarka Temple', 'location': 'Dwarka', 'description': 'Sacred Krishna temple and one of the four Char Dhams', 'image_url': 'https://images.unsplash.com/photo-1578021046445-3b7c8bdd16db?w=400', 'rating': 4.6, 'category': 'Temple', 'entry_fee': 'Free', 'contact': '+91-2892-234403', 'best_time': 'Oct-Mar'},
                {'name': 'Gir National Park', 'location': 'Junagadh', 'description': 'Last refuge of Asiatic lions in their natural habitat', 'image_url': 'https://images.unsplash.com/photo-1549366021-9f761d040a94?w=400', 'rating': 4.4, 'category': 'Wildlife', 'entry_fee': '₹300', 'contact': '+91-2877-285540', 'best_time': 'Dec-Apr'},
                {'name': 'Somnath Temple', 'location': 'Somnath', 'description': 'First of twelve Jyotirlinga shrines by the Arabian Sea', 'image_url': 'https://images.unsplash.com/photo-1578021046445-3b7c8bdd16db?w=400', 'rating': 4.7, 'category': 'Temple', 'entry_fee': 'Free', 'contact': '+91-2876-231727', 'best_time': 'Oct-Mar'}
            ]
        }

        # Add major destinations
        for state_name, destinations in major_destinations.items():
            for dest in destinations:
                dest['state'] = state_name
                destinations_data.append(dest)

        # Add generic destinations for other states
        other_states = ['Karnataka', 'Tamil Nadu', 'Rajasthan', 'Kerala', 'Uttar Pradesh', 'West Bengal', 'Punjab', 'Goa', 'Delhi', 'Andhra Pradesh']
        for state_name in other_states:
            for i in range(6):
                dest_types = ['Palace', 'Fort', 'Temple', 'Beach', 'Museum', 'Garden']
                categories = ['Heritage', 'Fort', 'Temple', 'Beach', 'Museum', 'Garden']

                destinations_data.append({
                    'name': f'{state_name} {dest_types[i]}',
                    'location': f'{state_name} City',
                    'description': f'Historic {dest_types[i].lower()} showcasing {state_name} culture and heritage',
                    'image_url': f'https://images.unsplash.com/photo-157700000{i}?w=400',
                    'rating': round(3.5 + (i * 0.2), 1),
                    'category': categories[i],
                    'entry_fee': '₹50' if i % 2 == 0 else 'Free',
                    'contact': f'+91-11-1111{i}{i}{i}{i}',
                    'best_time': 'Oct-Mar',
                    'state': state_name
                })

        # Create destinations
        for dest_data in destinations_data:
            state_name = dest_data.pop('state')
            dest_data['state_id'] = states[state_name].id
            destination = Destination(**dest_data)
            db.session.add(destination)

        # Create restaurants
        print("Creating restaurants...")
        for state_name, state in states.items():
            cuisines = ['Traditional', 'North Indian', 'South Indian', 'Chinese', 'Continental']
            restaurant_types = ['Royal', 'Street Food', 'Multi-Cuisine', 'Family', 'Heritage Cafe']

            for i in range(5):
                restaurant = Restaurant(
                    name=f'{state_name} {restaurant_types[i]} Restaurant',
                    location=f'{state_name} {"Heritage Area" if i == 0 else "Market Square" if i == 1 else "Commercial District" if i == 2 else "Residential Area" if i == 3 else "Old City"}',
                    description=f'Authentic {cuisines[i]} cuisine offering traditional flavors of {state_name}',
                    image_url=f'https://images.unsplash.com/photo-157000000{i}?w=400',
                    rating=round(3.8 + (i * 0.15), 1),
                    cuisine_type=cuisines[i],
                    price_range=['₹₹₹₹', '₹', '₹₹₹', '₹₹', '₹₹'][i],
                    contact=f'+91-11-222{i}{i}{i}{i}',
                    famous_dishes=f'{state_name} Special Thali, Regional Delicacies, Local Sweets',
                    state_id=state.id
                )
                db.session.add(restaurant)

        # Create hospitals
        print("Creating hospitals...")
        for state_name, state in states.items():
            hospital_names = ['Medical College', 'Heart Institute', 'General', 'Children', 'Eye Care Center']
            hospital_types = ['Teaching Hospital', 'Specialty', 'Multi-specialty', 'Pediatric', 'Eye Care']

            for i in range(5):
                hospital = Hospital(
                    name=f'{state_name} {hospital_names[i]} Hospital',
                    location=f'{state_name} {"Medical District" if i == 0 else "Healthcare Hub" if i == 1 else "City Center" if i == 2 else "Pediatric Zone" if i == 3 else "Vision Care Complex"}',
                    description=f'Quality healthcare services providing {hospital_types[i].lower()} medical care in {state_name}',
                    image_url=f'https://images.unsplash.com/photo-156000000{i}?w=400',
                    rating=round(4.0 + (i * 0.1), 1),
                    hospital_type=hospital_types[i],
                    specialties=['General Medicine, Surgery, Emergency Care', 'Cardiology, Heart Surgery, Cardiac Care', 'All Medical Specialties, ICU, Diagnostics', 'Pediatrics, Child Care, Vaccination', 'Ophthalmology, Eye Surgery, Vision Care'][i],
                    contact=f'+91-11-333{i}{i}{i}{i}',
                    emergency_services=i <= 2,  # First 3 have emergency services
                    bed_count=[800, 200, 400, 150, 50][i],
                    state_id=state.id
                )
                db.session.add(hospital)

        # Commit all data
        db.session.commit()

        print("\n" + "="*50)
        print("DATABASE SEEDED SUCCESSFULLY!")
        print("="*50)
        print(f"States: {State.query.count()}")
        print(f"Destinations: {Destination.query.count()}")
        print(f"Restaurants: {Restaurant.query.count()}")
        print(f"Hospitals: {Hospital.query.count()}")
        print("\nRun 'python app.py' to start the application!")

if __name__ == '__main__':
    seed_data()