# init.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


# Initialisation de la base de données SQLAlchemy 
db = SQLAlchemy()

def create_app():
    
    UPLOAD_FOLDER = './ftp' # Utilisation de variable pour l'upload de fichier dans le cadre de transftert de fichier
    
    app = Flask(__name__) # déclaration du nom de l'application
    

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO' # Clé secrete de l'application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' # Chemin vers la base de données
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Mappage du dossier FTP

    db.init_app(app) # Démarrage de la base de données

    login_manager = LoginManager()  # Liens entre FLask-Login et Netway-Management
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
       
        return User.query.get(int(user_id))

    # Créations de routes dans le fichier auth.py
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Créations de routes dans le fichier main.py
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app