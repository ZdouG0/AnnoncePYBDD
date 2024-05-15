from createdatabase import *


class CUsers() :
    
    

    def __init__(self,email='', password='', number=0,nom='') :
        #creation de l'objet dans la BAse de donnees
        string = "SELECT * from Users WHERE Users.UserEmail ='"+email+"'"
        sql = text(string)
        result = session.execute(sql)
        for user in result :
            self.UserId = user.IdUser
        self.UserName = nom
        self.UserEmail = email
        self.UserPassword = password
        self.UserNumber = number

    def makeoffer():
        pass

    def ResponseOffer():
        pass
    
    def ViewOffer(self):
        string = "SELECT * from Offers WHERE Offers.IdUserVendeur ="+str(self.UserId)
        sql = text(string) 
        result = session.execute(sql)
        if result.rowcount == 0 :
            print("Aucune offre !")
        else :
            for offer in result :
                #get le nom de l'acheteur
                string2 = "SELECT * from Users WHERE Users.IdUser ="+str(offer.IdUserAcheteur)
                print(string2)
                sql2 = text(string2) 
                result2 = session.execute(sql2)
                Acheteur=0
                for utili in result2 :
                    Acheteur = utili.UserName
                #get le nom de l'offre
                string3 = "SELECT * from Advertisement WHERE Advertisement.IdAd ="+str(offer.IdAd)
                sql3 = text(string3) 
                result3 = session.execute(sql3)
                Annonce=0
                for annn in result3 :
                    Annonce = annn.AdName
                print("    >>>",offer.IdOffer,". Offre de",offer.OfferPrice,"€ par",Acheteur,"pour votre annonce :",Annonce)
                if offer.OfferAcceptation ==1 :
                    string="Acceptée"
                else :
                    string="Refusée"
                print("                 ---> Etat :",string)

    def __del__(self):
        print("L'objet de la classe Cusers a été detruit")

