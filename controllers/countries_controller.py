from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository


countries_blueprint = Blueprint('countries', __name__)

# Add country
@countries_blueprint.route('/countries/new', methods=['GET'])
def show_countries(id):
    return render_template('countries/show.html')

