from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.holiday import Holiday
import repositories.holiday_repository as holiday_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository


holidays_blueprint = Blueprint('holidays', __name__)


@holidays_blueprint.route('/holidays')
def holidays():
    holidays = holiday_repository.select_all()
    return render_template('holidays/index.html', all_holidays = holidays)

# NEW
# GET '/holidays/new'
@holidays_blueprint.route('/holidays/new', methods=['GET'])
def new_holiday():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    users = user_repository.select_all()
    return render_template('holidays/new.html', cities = cities, countries = countries, users = users)

# CREATE
# POST '/holidays'
@holidays_blueprint.route('/holidays', methods=['POST'])
def create_holiday():
    type = request.form['type']
    country_id = request.form['country_id']
    city_id = request.form['city_id']
    review = request.form['review']
    user_id = request.form['user_id']
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)
    user = user_repository.select(user_id)
    holiday = Holiday(type, country, city, review, user)
    holiday_repository.save(holiday)
    return redirect('/holidays')







