from flask import Blueprint, render_template, redirect, url_for

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def home():
    return render_template('home.html')