from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.country import City

import repositories.city_repository as city_repository


cities_blueprint = Blueprint('cities', __name__)

# Add country
@cities_blueprint.route('/cities/new', methods=['GET'])
def show_countries():
    return render_template('cities/new_city.html')

@cities_blueprint.route('/cities', methods=['POST'])
def create_country():
    name = request.form['name']
    city = City(name)
    city_repository.save(city)
    return redirect('/holidays')