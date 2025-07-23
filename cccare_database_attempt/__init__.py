from flask import Flask
from flask_wtf.csrf import CSRFProtect #WTForms requires csrf protection to process each request securely
 #the . indicates we're importing from a local file in the same folder
from .extensions import db #import in the SQLAlchemy database session
from .sensor_monitor import start_serial_thread 

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__) 
    # Configure the app
    #set up the database file location
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/Jessica/Documents/S25_HealthTech_Prep/cccare_database_attempt/test_exercise.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # disables a feature that tracks changes, which is not needed in this case
    app.config["SECRET_KEY"] = "securitycode" #secret key is required by WTForms for the CSRF token
    #initialize and attach the CSRF and database extensions to the app
    csrf.init_app(app)
    db.init_app(app)
    
    # imports and attaches the blueprint (pages.bp) that holds all the routes in the app
    from . import pages
    app.register_blueprint(pages.bp)

    #start background thread for Arduino sensor data
    start_serial_thread(app)

    return app

