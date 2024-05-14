
from createdatabase import *

class CUsers() :
    
    

    def __init__(self,email='', password='', number=0,nom='') :
        #creation de l'objet dans la BAse de donnees
        user=Users(UserName=nom,UserEmail=email,UserPassword=password,UserPhone=number)
        session.add(user)
        session.commit()
        self.UserName = nom
        self.UserEmail = email
        self.UserPassword = password
        self.UserNumber = number

    def makeoffer():
        pass

    def ResponseOffer():
        pass
    
    def ViewOffer():
        pass

    def __del__(self):
        print("L'objet de la classe Cusers a été detruit")

