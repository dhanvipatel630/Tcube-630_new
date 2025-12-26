from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import Optional, Length

class SearchForm(FlaskForm):
    query = StringField('Search', validators=[Optional(), Length(max=100)],
                       render_kw={"placeholder": "Search states..."})
    submit = SubmitField('Search')

class DestinationFilterForm(FlaskForm):
    search = StringField('Search Destinations', validators=[Optional(), Length(max=100)],
                        render_kw={"placeholder": "Search destinations..."})
    category = SelectField('Category', choices=[('', 'All Categories')], validators=[Optional()])
    rating_min = SelectField('Minimum Rating', choices=[
        ('', 'Any Rating'),
        ('3.0', '3+ Stars'),
        ('3.5', '3.5+ Stars'),
        ('4.0', '4+ Stars'),
        ('4.5', '4.5+ Stars')
    ], validators=[Optional()])
    sort_by = SelectField('Sort By', choices=[
        ('rating', 'Highest Rated'),
        ('name', 'Name (A-Z)'),
        ('visit_count', 'Most Popular'),
        ('created_at', 'Recently Added')
    ], default='rating')
    featured_only = BooleanField('Featured Only')
    submit = SubmitField('Apply Filters')

class RestaurantFilterForm(FlaskForm):
    search = StringField('Search Restaurants', validators=[Optional(), Length(max=100)],
                        render_kw={"placeholder": "Search restaurants..."})
    cuisine_type = SelectField('Cuisine', choices=[('', 'All Cuisines')], validators=[Optional()])
    price_range = SelectField('Price Range', choices=[
        ('', 'Any Price'),
        ('₹', 'Budget (₹)'),
        ('₹₹', 'Moderate (₹₹)'),
        ('₹₹₹', 'Expensive (₹₹₹)'),
        ('₹₹₹₹', 'Luxury (₹₹₹₹)')
    ], validators=[Optional()])
    rating_min = SelectField('Minimum Rating', choices=[
        ('', 'Any Rating'),
        ('3.0', '3+ Stars'),
        ('3.5', '3.5+ Stars'),
        ('4.0', '4+ Stars'),
        ('4.5', '4.5+ Stars')
    ], validators=[Optional()])
    delivery = BooleanField('Delivery Available')
    sort_by = SelectField('Sort By', choices=[
        ('rating', 'Highest Rated'),
        ('name', 'Name (A-Z)'),
        ('avg_cost_for_two', 'Price (Low to High)'),
        ('visit_count', 'Most Popular')
    ], default='rating')
    featured_only = BooleanField('Featured Only')
    submit = SubmitField('Apply Filters')

class HospitalFilterForm(FlaskForm):
    search = StringField('Search Hospitals', validators=[Optional(), Length(max=100)],
                        render_kw={"placeholder": "Search hospitals..."})
    hospital_type = SelectField('Type', choices=[('', 'All Types')], validators=[Optional()])
    ownership = SelectField('Ownership', choices=[
        ('', 'Any'),
        ('Government', 'Government'),
        ('Private', 'Private'),
        ('Trust', 'Trust/NGO')
    ], validators=[Optional()])
    emergency_only = BooleanField('Emergency Services Only')
    blood_bank = BooleanField('Blood Bank Available')
    rating_min = SelectField('Minimum Rating', choices=[
        ('', 'Any Rating'),
        ('3.0', '3+ Stars'),
        ('3.5', '3.5+ Stars'),
        ('4.0', '4+ Stars'),
        ('4.5', '4.5+ Stars')
    ], validators=[Optional()])
    sort_by = SelectField('Sort By', choices=[
        ('rating', 'Highest Rated'),
        ('name', 'Name (A-Z)'),
        ('bed_count', 'Bed Count'),
        ('established_year', 'Oldest First')
    ], default='rating')
    featured_only = BooleanField('Featured Only')
    submit = SubmitField('Apply Filters')
