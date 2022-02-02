class Holiday:

    def __init__(self, holiday_type, country, city, transport, currency, review, user, id = None):
        self.holiday_type = holiday_type
        self.country = country
        self.city = city
        self.transport = transport
        self.currency = currency
        self.review = review
        self.user = user
        self.id = id