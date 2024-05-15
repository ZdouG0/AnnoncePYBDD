from createdatabase import*
from ClssPerson import *

#creation d'une personne
#init_database()
test = CPerson()

print("\n*********************************************************************************************\n*                                                                                           *\n*    Bienvenue dans notre interface de vente de voiture entre Particulier                   *\n*                                                                                           *\n*********************************************************************************************\n")


print ("________________________ Catalogues __________________________\n")
sql = text ("SELECT * FROM Advertisement;")
result = session.execute(sql)

for annonce in result :
    print ("    >>> " ,annonce.IdAd,".",annonce.AdName,'\n')

repfiltre=''
repfiltre = input("Voulez vous appliquer des filtres [Y/N]:")
FiltreOk=False
while FiltreOk ==False:
    
    if repfiltre != 'Y' and repfiltre != 'N' and repfiltre != 'y' and repfiltre != 'n':
        repfiltre = input("Entree incorrect ! Veuillez reesayer :")
    else :
        FiltreOk = True
if repfiltre == 'y' or repfiltre=='Y':
    print("Veuillez choisir vos filtres :")

repfiltre = input("Voulez vous vous connecter afin de creer et gerer vos annonces [Y/N]:")
FiltreOk=False
while FiltreOk ==False:
    
    if repfiltre != 'Y' and repfiltre != 'N' and repfiltre != 'y' and repfiltre != 'n':
        repfiltre = input("Entree incorrect ! Veuillez reesayer :")
    else :
        FiltreOk = True
if repfiltre == 'y' or repfiltre=='Y':
    Utilisateur=test.login()
    repcreate = input("Voulez vous creer une annonce ? [Y/N]")
    RepOk=False
    while RepOk ==False:
        
        if repcreate != 'Y' and repcreate != 'N' and repcreate != 'y' and repcreate != 'n':
            repcreate = input("Entree incorrect ! Veuillez reesayer :")
        else :
            RepOk = True
    if repcreate == 'y' or repcreate=='Y':
        Utilisateur.create_announce()
    repViewAnnonce = input("Voulez vous gerer les offres ? [Y/N]")
    RepOk=False
    while RepOk ==False:
        
        if repViewAnnonce != 'Y' and repViewAnnonce != 'N' and repViewAnnonce != 'y' and repViewAnnonce != 'n':
            repViewAnnonce = input("Entree incorrect ! Veuillez reesayer :")
        else :
            RepOk = True
    if repViewAnnonce == 'y' or repViewAnnonce=='Y':
        Utilisateur.ViewOffer()

idannonce = int(input("Entrez l'identifiant de l'annonce que vous souhaitez consulter :"))
requete = "SELECT * FROM Advertisement WHERE IdAd="+str(idannonce)+";"
sql = text (requete)
result = session.execute(sql)
requeteOk=False
while requeteOk==False :
    if result.rowcount==0 :
        idannonce =int(input('Entree Incorrect ! Veuillez reesayer :'))
    else:
        requeteOk = True
for annonce in result :
    print("-------------------- Annonce ---------------------------",)
    #information dans la table advertisment (description apparait plus tard)
    print("Titre de l'annonce :",annonce.AdName)
    print("Mode de payement :",annonce.AdTypePayement)
    print("Localisation :",annonce.AdLocalisation)
    print("Prix :",annonce.AdPrice)
    #information dans la table cars
    requetecar = "SELECT * FROM Cars WHERE IdCar="+str(annonce.IdCar)+";"
    sql = text (requetecar)
    requetecar = session.execute(sql)
    for car in requetecar:
        print("Marque du vehicule :",car.CarBrand)
        print("Modele :",car.CarModel)
        print("Nombre de place :",car.CarNumberDoors)
        print("Type de Carburant :",car.CarFuel)
        print("Date de sortie :",car.CarRelease)
        print("Etat du vehicule :",car.CarState)
        print("Kilometrage :",car.CarKilometer)
    #info de categorie
    requetecat = "SELECT * FROM Category WHERE IdCat="+str(annonce.IdCat)+";"
    sql = text(requetecat)
    requetecat = session.execute(sql)
    for cat in requetecat:
        print("Categorie :",cat.CatName)
    #info Vendeur
    requeteVend = "SELECT * FROM Users WHERE IdUser="+str(annonce.IdUser)+";"
    sql = text (requeteVend)
    requeteVend = session.execute(sql)
    for Vendeur in requeteVend:
        print("Information Vendeur")
        print("Nom Vendeur :",Vendeur.UserName)
        print("Numero de Telephone :",Vendeur.UserPhone)
    print("Description du vehicule :",annonce.AdDescription)
    print("\n\n")




result = session.execute(sql) 
session.commit()
#test.signin()