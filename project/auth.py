# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db
from itertools import *
from .scanthread import scan
import sys
import os
from werkzeug.utils import secure_filename


auth = Blueprint('auth', __name__) # Définition des routes 

@auth.route('/login') #Pages de connexion
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post(): # Recuperations des informations rentrées par l'utilisateur
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first() #  Requêtes SQLALCHEMY pour chercher l'utilisateur en fonction de l'adresse mail
    role = user.role
    

    # On vérifie que l'utilisateur existe
    # On compare le mot de passe dans la base de données en enlevant le hash, si cela ne correspond pas il retourne une erreur 
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # Si les logins et mot de passes sont bon, nous redirigeons l'utilisateur en fonction de son rôle
    if role == "Administrateur-Supreme" : 
        login_user(user, remember=remember)
        return redirect(url_for('main.profile1'))
    
    if role == "Administrateur-Classique" : 
        login_user(user, remember=remember)
        return redirect(url_for('main.profile2'))
    
    if role == "User" : 
        login_user(user, remember=remember)
        return redirect(url_for('main.profile3'))
    


@auth.route('/signup') # Page d'inscription
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST']) # Pages d'inscription quand le bouton a été activé
def signup_post():

    email = request.form.get('email') # Récupération des entrées utilisateurs
    name = request.form.get('name')
    password = request.form.get('password')
    role = request.form.get('role')

    user = User.query.filter_by(email=email).first() # On vérifie que l'email n'est pas dans la base de données

    if user: # Si l'email est déjà dans la base de données, une erreur apparait  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # Créations de l'utilisateur dans la base de données avec un mot de passe hashé
    new_user = User(email=email, name=name, role=role, password=generate_password_hash(password, method='sha256'))

    # Ajout de l'utilisateur dans la base de données
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login')) # Redirection vers la page de connexion

@auth.route('/logout') # Fonction déconnexion
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/password-change') # Pages changement de mot de posse
@login_required # On doit être connecter pour accéder à cette page
def changement():
    return render_template('password-change.html')


@auth.route('/password-change', methods=['POST']) # Fonction qui s'active quand l'utilisateur appuis sur le bouton modifier
@login_required
def changement_post():
    old_pwd = request.form.get('old') # Récupération des données utilsateurs
    new1 = request.form.get('new1')
    new2 = request.form.get('new2')
    email_pwd = current_user.email
    flash (email_pwd)
    
    if new1 != new2: # Comparaison entre les deux nouveaux mot de passe rentré : ils doivent correspondre
        flash('Les mots de passe sont differents')
        return redirect(url_for('auth.changement'))
        
    
    test_pwd = User.query.filter_by(email=email_pwd).first() # Récupération de l'utilisateur
    
    if not check_password_hash(test_pwd.password, old_pwd):  # Comparaison entre le mot de passe dans la base de données et le mot de passe actuel
        flash('Mot de passe incorrect')
    
    change_pwd = User.query.filter_by(email=email_pwd).update({User.password: generate_password_hash(new2, method='sha256') }) # Changement du mot de passe dans la base de données
    

    db.session.commit() # Application des changements
    
    return redirect(url_for('auth.login')) # Redirection vers la page de connexion


@auth.route('/management') # Page management des utilisateurs
@login_required
def management():
    ids = User.query.with_entities(User.id).all() # On interroge la base de données en récuperrant tout les ID
    nom = User.query.with_entities(User.name).all()
    mail = User.query.with_entities(User.email).all()
    role = User.query.with_entities(User.role).all()
    
    
    return render_template('mngt.html', ids=ids, nom=nom, mail=mail, role=role, zip=zip ) # Redirection vers la page html et déclaration des variables


@auth.route('/management', methods=['POST']) # Suppression d'utilisateur
@login_required
def management_post():
    
    email=request.form.get('suppr') # Recuperation de l'utilisateur à supprimer
    
    """ User.query.filter_by(email=email).delete() """
    suppr=User.query.filter_by(email=email).first() # Recherche dans la base de données en fonction de l'email
    
    db.session.delete(suppr) # Suppression de l'utilisateur
    db.session.commit() # Application des changements dans la base de données
    flash(email,'a été supprimé')



    
    return redirect(url_for('auth.management'))


@auth.route('/port') # Scan de port : Non fonctionnel
@login_required
def scan_port():
    
    read_scan=print(list)
    
    """read_scan=print(sys.stdout.read()) 
    read_scan=sys.stdout """
    
    return render_template('port.html', read_scan=read_scan)


def allowed_file(filename): # Déclarations des exetensions de fichier autorisé sur le partage de fichier
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','docx'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@auth.route('/ftp', methods=['GET', 'POST']) # Page de transfert de fichier
@login_required
def ftp():
    
    if request.method == 'POST' and request.files['file'] is not None:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('/srv/Python-NetWay/project/ftp', filename))
            return redirect(url_for('auth.ftp', name=filename))
        
    path = '/srv/Python-NetWay/project/ftp' # Mappage du dossier FTP
    file = os.listdir(path) # Liste des fichier dans la variable $path

    if request.method == 'POST' and request.form.get('suppr') is not None: # Suppressions des fichiers : si dans l'entête HTTP le champs suppr est rempli, le IF continue
        file_delete = str(request.form.get('suppr')) # Recuperation du nom du fichier à supprimer depuis l'entête HTML
        path_file = path + '/' + file_delete # Customisation du chemin des fichiers 
        os.remove(path_file) # Suppression du fichier
        return redirect(url_for('auth.ftp')) # Actualisation de la page
        
    return render_template('ftp.html', file=file)

@auth.route('/srv/Python-NetWay/project/ftp/<filename>') # Fonction Download
@login_required
def files_download(filename):
    return send_file('ftp/'+filename) # Envoi du fichier