from db.run_sql import run_sql
from models.country import Country
from models.city import City
from models.user import User


def save(user):
    sql = "INSER INTO users( name ) VALUES ( %s ) RETURNING id"
    values = [user.name]
    results = run_sql( sql, values)
    user.id = results[0]['id']
    return user