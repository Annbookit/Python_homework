class Address:

    def __init__(self, indx, city, strit, home, apart):
        self.indx = indx
        self.city = city
        self.strit = strit
        self.home = home
        self.apart = apart

    def __str__(self):
        return f"Индекс: {self.indx}, Город: {self.city}, улица: {self.strit}, дом: {self.home}, квартира: {self.apart}"
    

