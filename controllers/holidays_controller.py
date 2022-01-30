from flask import Flask, redirect, render_template, request
from flask import Blueprint
from repositories import holiday_repository, city_repository, country_repository, user_repository
from models.holiday import Holiday

holidays_blueprint = Blueprint('holidays', __name__)


@holidays_blueprint.route('/holidays')
def holidays():
    holidays = holiday_repository.select_all()
    return render_template('holidays/index.html', all_holidays = holidays)





