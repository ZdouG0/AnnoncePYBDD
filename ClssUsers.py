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

    def makeoffer(self,IdAnnonce):
        string = "SELECT * from Advertisement WHERE Advertisement.IdAd ="+str(IdAnnonce)
        sql = text(string)
        result = session.execute(sql)
        idVendeur=0
        for ad in result :
            idVendeur = ad.IdUser
        prix = float(input("Entrer le montant de votre offre :"))
        quest ="INSERT INTO Offers(OfferAcceptation,OfferPrice,IdUserAcheteur,IdUserVendeur,IdAd) VALUES (False,"+str(prix)+","+str(self.UserId)+","+str(idVendeur)+","+str(IdAnnonce)+")"
        sql = text(quest)
        result = session.execute(sql)
        session.commit()
        print("Creation de votre Offre reussie !")



    def ResponseOffer(self):
        ReponseOK=False
        while ReponseOK == False :
            Reponse =int(input("Entrer l'identifiant de l'offre dont vous voulez changer l'etat"))
            string = "SELECT * from Offers WHERE Offers.IdUserVendeur ="+str(self.UserId)+" AND Offers.IdOffer ="+str(Reponse)
            sql = text(string)
            result = session.execute(sql)
            if result.rowcount == 0 :
                print("Entrée incorrect veuillez reesayer!")
            else :
                ReponseOK = True
        for offer in result :
            if offer.OfferAcceptation == 0 :
                string = "UPDATE Offers SET Offers.OfferAcceptation = True WHERE Offers.IdOffer ="+str(Reponse)
            else :
                string = "UPDATE Offers SET Offers.OfferAcceptation = False WHERE Offers.IdOffer ="+str(Reponse)
            sql = text(string)
            result = session.execute(sql)
            session.commit()
        self.ViewOffer()
            
        
    
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
            repfiltre = input("Voulez vous interagir avec vos offres [Y/N]:")
            FiltreOk=False
            while FiltreOk ==False:
                if repfiltre != 'Y' and repfiltre != 'N' and repfiltre != 'y' and repfiltre != 'n':
                    repfiltre = input("Entree incorrect ! Veuillez reesayer :")
                else :
                    FiltreOk = True
                if repfiltre == 'y' or repfiltre=='Y':
                    self.ResponseOffer()


    def create_announce(self):
        print("--------- Menu de création d'annonce ---------")
        print ("\najout de votre Vehicule :")
        Marque = input("Veuillez entrer la marque de votre véhicule : ")
        Model = input("Veuillez entrer le modèle de votre véhicule : ")
        NombrePorte = int(input("Veuillez entrer le nombre de portes de votre véhicule : "))
        Carburant = input("Veuillez entrer le carburant de votre véhicule : ")
        Sortie = input("Veuillez entrer l'année de sortie de votre véhicule : ")
        Etat = input("Veuillez entrer l'état de votre véhicule : ")
        Km = int(input("Veuillez entrer le kilométrage de votre véhicule : "))
        requete = "INSERT INTO Cars(CarBrand,CarModel,CarNumberDoors,CarFuel,CarRelease,CarState,CarKilometer) Values('"+Marque+"','"+Model+"',"+str(NombrePorte)+",'"+Carburant+"',"+str(Sortie)+",'"+Etat+"',"+str(Km)+")"
        sql = text (requete)
        result = session.execute(sql)
        session.commit()
        requete3 = "SELECT * FROM Cars ORDER BY IdCar DESC LIMIT 1;"
        sql3 = text (requete3)
        result3 = session.execute(sql3)
        for car in result3 :
            ide_car=car.IdCar
        requeteOk=False
        print("finalisation de l'annonce :")
        AdName = input("Veuillez entrer le nom de l'annonce : ")
        AdTypePayement = input("Veuillez entrer le type de paiement de l'annonce : ")
        AdLocalisation = input("Veuillez entrer la localisation de l'annonce : ")
        AdPrice = float(input("Veuillez entrer le prix de l'annonce : "))
        AdDescription = input("Veuillez entrer la description de l'annonce : ")
        print ("List categorie :") 
        sql = text("SELECT * from Category")
        result = session.execute(sql)
        for cate in result :
            print ("    >>> ",cate.IdCat,cate.CatName)
        idact = int(input("Entrez l'identifiant de la categorie que vous souhaitez ajouter :"))
        requete2 = "SELECT * FROM Category WHERE Category.IdCat="+str(idact)+";"
        sql2 = text (requete2)
        result2 = session.execute(sql2)
        requeteOk=False
        while requeteOk==False :
            if result2.rowcount==0 :
                idannonce =int(input('Entree Incorrect ! Veuillez reesayer :'))
            else:
                requeteOk = True
        categorie_final =0
        for choice_cat in result2 :
            categorie_final = choice_cat.IdCat
        requete4 = "SELECT * FROM Users WHERE Users.UserEmail='"+self.UserEmail+"';"
        sql4 = text (requete4)
        result4 = session.execute(sql4)
        for userrr in result4 :
            userId = userrr.IdUser
        query_announce = "INSERT INTO Advertisement(AdName,AdTypePayement,AdLocalisation,AdPrice,AdDescription,IdUser,IdCar,IdCat) VALUES('"+AdName+"','"+AdTypePayement+"','"+AdLocalisation+"',"+str(AdPrice)+",'"+AdDescription+"',"+str(userId)+","+str(ide_car)+","+str(categorie_final)+");"
        sql = text (query_announce)
        resilt = session.execute(sql)
        session.commit()


