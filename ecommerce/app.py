from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/images/products'

db = SQLAlchemy(app)

# Import models
from models.user import User
from models.product import Product
from models.category import Category
from models.cart import Cart, CartItem
from models.order import Order, OrderItem

# Import routes
from routes import user_routes, product_routes, cart_routes, order_routes, admin_routes

# Register blueprints
app.register_blueprint(user_routes.bp)
app.register_blueprint(product_routes.bp)
app.register_blueprint(cart_routes.bp)
app.register_blueprint(order_routes.bp)
app.register_blueprint(admin_routes.bp)

@app.route('/')
def index():
    featured_products = Product.query.filter_by(featured=True).limit(8).all()
    categories = Category.query.all()
    return render_template('index.html', featured_products=featured_products, categories=categories)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)