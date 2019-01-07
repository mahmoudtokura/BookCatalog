from flask import Blueprint, render_template, redirect, url_for
from src.blueprint.catalog.models import Publication

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def display_all_books():
    return render_template('all_books.html')


@main_blueprint.route('/test')
def display_all_publications():
    pass