from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


cities_blueprint = Blueprint('cities', __name__)

# Add city
@cities_blueprint.route('/cities/new', methods=['GET'])
def show_cities():
    countries = country_repository.select_all()
    return render_template('cities/new_city.html', all_countries = countries)

@cities_blueprint.route('/cities', methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    city = City(name, country)
    city_repository.save(city)
    return redirect('/holidays/new')