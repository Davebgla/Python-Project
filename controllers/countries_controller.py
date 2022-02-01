from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository


countries_blueprint = Blueprint('countries', __name__)

# Add country
@countries_blueprint.route('/countries/new', methods=['GET'])
def show_countries():
    return render_template('countries/new_country.html')

@countries_blueprint.route('/countries', methods=['POST'])
def create_country():
    name = request.form['name']
    country = Country(name)
    country_repository.save(country)
    return redirect('/holidays')