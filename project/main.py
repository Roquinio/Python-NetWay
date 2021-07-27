# main.py flask

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)  # Définition des routes 

@main.route('/') # Page d'accueil
def index():
    return render_template('index.html')

@main.route('/profile') # Page de profil basique
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, role=current_user.role)

@main.route('/profile1') # Page de profil Administrateur Supreme 
@login_required
def profile1():
    return render_template('as.html', name=current_user.name, role=current_user.role)

@main.route('/profile2') # Page de profil Administrateur Classique
@login_required
def profile2():
    return render_template('admin.html', name=current_user.name, role=current_user.role)

@main.route('/profile3') # Page de profil User
@login_required
def profile3():
    return render_template('User.html', name=current_user.name, role=current_user.role)
