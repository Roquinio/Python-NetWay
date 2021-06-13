from flask import Flask
from . import db

main = Blueprint('main', __name__)




@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile')
def profile():
    return 'Profile'



