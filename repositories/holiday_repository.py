from unittest import result
from controllers import country
from db.run_sql import run_sql
from models.holiday import Holiday
from models.country import Country
from models.city import City
from models.user import User
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.user_repository as user_repository


def save(holiday):
    sql = "INSERT INTO holidays (type, country_id, city_id, review, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [holiday.type, holiday.country.id, holiday.city.id, holiday.review, holiday.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    holiday.id = id
    return holiday


def select_all():
    holidays = []

    sql = "SELECT * FROM holidays"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = city_repository.select(row['city_id'])
        user = user_repository.select(row['user_id'])
        holiday = Holiday(row['type'], country, city, row['review'], user, row['id'])
        holidays.append(holiday)
    return holidays


def select(id):
    holiday = None
    sql = "SELECT * FROM holidays WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = city_repository.select(result['city_id'])
        user = user_repository.select(result['user_id'])
        holiday = Holiday(result['type'], country, city, result['review'], user, result['id'])
    return holiday


def delete_all():
    sql = "DELETE FROM holidays"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM holidays WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(holiday):
    sql = "UPDATE holidays SET (type, country_id, city_id, review, user_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [holiday.type, holiday.country.id, holiday.city.id, holiday.review, holiday.user.id, holiday.id]
    run_sql(sql, values)