from db.run_sql import run_sql
from models.country import Country
from models.city import City
from models.user import User


def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING *"
    values = [user.name]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user


def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['name'], result['id'])
    return user


# def delete_all():
#     sql = "DELETE FROM users"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE  FROM users WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(user):
#     sql = "UPDATE users SET (name) = (%s) WHERE id = %s"
#     values = [user.name, user.id]
#     run_sql(sql, values)