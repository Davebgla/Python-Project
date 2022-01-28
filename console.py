import pdb
from models.country import Country
from models.user import User

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

pdb.set_trace()