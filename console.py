import pdb
from models.city import City
from models.country import Country
from models.holiday import Holiday
from models.user import User

import repositories.holiday_repository as holiday_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

#USERS CREATED
user1 = User("Claire")
user_repository.save(user1)
user2 = User("Dave")
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


# HOLIDAYS CREATED
holiday1 = Holiday("Summer Holiday", country1, city1, "Very hot! Amazing food! Hotel was 5 star. Would go back!", user1)
holiday_repository.save(holiday1)
holiday2 = Holiday("Spring 2022 Holiday", country2, city2, "Can't wait to go back! NYC is my favourite city!", user2)
holiday_repository.save(holiday2)
holiday3 = Holiday("Long Weekend", country3, city3, "Possibly the best city in Europe! So much to do! Especially enjoyed the drinking!", user3)
holiday_repository.save(holiday3)
holiday4 = Holiday("Winter 2022", country4, city4, "Still not been. Looking forward to it but I've heard it's cold", user4)
holiday_repository.save(holiday4)






pdb.set_trace()