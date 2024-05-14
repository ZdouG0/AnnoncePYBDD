
from createdatabase import *

class CAdvertisement :

    def __init__(self,name, TypePayement,Localisation,Price,Description,User,Car,Cat):
        self.AdName = name
        self.AdTypePayement = TypePayement
        self.AdLocalisation = Localisation
        self.AdPrice = Price
        self.AdDescription= Description
        self.User=User
        self.IdCar=Car
        self.IdCat=Cat
