import pdb
from models.city import City
from models.country import Country
from models.user import User


import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

#USERS CREATED
user1 = User("Claire")
user_repository.save(user1)
user2 = User("Erin")
user_repository.save(user2)
user3 = User("Sean")
user_repository.save(user3)
user4 = User("Scott")
user_repository.save(user4)


# COUNTRIES CREATED
country1 = Country("Greece")
country_repository.save(country1)
country2 = Country("USA")
country_repository.save(country2)
country3 = Country("Spain")
country_repository.save(country3)
country4 = Country("Denmark")
country_repository.save(country4)


# CITIES CREATED
city1 = City("Athens", country1)
city_repository.save(city1)
city2 = City("New York City", country2)
city_repository.save(city2)
city3 = City("Barcelona", country3)
city_repository.save(city3)
city4 = City("copenhagen", country4)
city_repository.save(city4)

pdb.set_trace()