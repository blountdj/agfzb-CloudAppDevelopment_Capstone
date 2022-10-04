from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class CarModel(models.Model):

    MODEL_TYPE = (
        ('SEDAN','Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    )

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    dealer_id = models.IntegerField()
    caratype = models.CharField(max_length=50, choices=MODEL_TYPE, default='SUV')
    year = models.DateField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year, sentiment):
        self.name = name
        self.dealership = dealership
        self.review = review
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment

    def __str__(self):
        return "Review: " + self.review