class Holiday:

    def __init__(self, type, country, city, review, user, id = None):
        self.name = type
        self.country = country
        self.city = city
        self.review = review
        self.user = user
        self.id = id