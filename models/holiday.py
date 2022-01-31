class Holiday:

    def __init__(self, holiday_type, country, city, review, user, id = None):
        self.holiday_type = holiday_type
        self.country = country
        self.city = city
        self.review = review
        self.user = user
        self.id = id