import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_migrate import Migrate
from models import db, UploadedFile, CalendarEvent, Studyflow, User, Note
from datetime import datetime
from forms import LoginForm
from routes import main_bp
from NoteTakingSystem import NoteTakingSystem
from calendar_function import *
from werkzeug.security import generate_password_hash, check_password_hash

def create_app():
    app = Flask(__name__)

    # Absolute path to instance folder and DB file
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'instance', 'servicebases.db')
    os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['UPLOAD_FOLDER'] = 'uploads'

    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(main_bp)

    return app

# Initialize app and database
app = create_app()
note_system = NoteTakingSystem()

# Create tables on startup
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")

# Home route
@app.route('/')
def home():
    return render_template('index.html', title='Service Base')

# Static database page route
@app.route('/database')
def database_page():
    return render_template('database.html')

if __name__ == '__main__':
    # Print all registered routes
    print("Registered routes:")
    print(app.url_map)

    # Run the app
    app.run(debug=True)


    

