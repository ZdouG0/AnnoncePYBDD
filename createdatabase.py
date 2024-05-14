from sqlalchemy import create_engine, Column,Integer,String
from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine("mysql+mysqlconnector://root:password@127.0.0.1/voiturebdd", echo= None)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session= Session()



sql = text("DROP TABLE Users, Cars, Category,Advertisement,Offers;")
result = session.execute(sql) 
#Definition de la Table Users

class Users(Base) :
    __tablename__ = 'Users'

    IdUser = Column(Integer,primary_key=True)
    UserName = Column(String(50))
    UserEmail = Column(String(50), unique=True)
    UserPassword = Column(String(50))
    UserPhone = Column(String(10))


class Cars(Base) :
    __tablename__ = 'Cars'

    IdCar = Column(Integer,primary_key=True)
    CarBrand = Column(String(50))
    CarModel = Column(String(50))
    CarNumberDoors = Column(Integer)
    CarFuel = Column(String(50))
    CarRelease = Column(String(50))
    CarState = Column(String(50))
    CarKilometer = Column(Integer)

class Category(Base) :
    __tablename__ = 'Category'

    IdCat = Column(Integer,primary_key=True)
    CatName = Column(String(50))


class Advertisement(Base):

    __tablename__ = 'Advertisement'

    IdAd = Column(Integer,primary_key=True)
    AdName = Column(String(50))
    AdTypePayement = Column(String(50))
    AdLocalisation = Column(String(50))
    AdPrice = Column(Float)
    AdDescription = Column(String(1500))
    IdUser = Column(Integer, ForeignKey('Users.IdUser'), nullable=False)
    IdCar = Column(Integer, ForeignKey('Cars.IdCar'),unique=True, nullable=False)
    IdCat = Column(Integer, ForeignKey('Category.IdCat'), nullable=False)


class Offers(Base) :

    __tablename__ = 'Offers'

    IdOffer = Column(Integer,primary_key=True)
    OfferAcceptation = Column(Boolean)
    OfferPrice = Column(Integer)
    IdUserAcheteur = Column(Integer, ForeignKey('Users.IdUser'))
    IdUserVendeur = Column(Integer, ForeignKey('Users.IdUser'))
    IdAd = Column(Integer, ForeignKey('Advertisement.IdAd'),nullable=False) 


Base.metadata.create_all(engine)  


#ajout de données initial dans la base de donnée :


sql = text("INSERT INTO category(IdCat,CatName) VALUES (1,'SUV'),(2,'Berline'),(3,'Coupe'),(4,'Citadine'),(5,'Sportive');")
result = session.execute(sql) 

sql = text ("INSERT INTO Cars(IdCar,CarBrand,CarModel,CarNumberDoors,CarFuel,CarRelease,CarState,CarKilometer) Values(1,'Porsche','718 Cayman Type 987',3,'Essence',2007,'Tres bonne etat',110096),(2,'Tesla','Model 3 phase 2',5,'Electrique',2022,'Tres bonne etat',25882);")
result = session.execute(sql) 

sql = text ("INSERT INTO Users(IdUser,UserName,UserEmail,UserPassword,UserPhone) VALUES(1,'Siddikh','sid@gmail.com','password',0612355458),(2,'Milan','mil@gmail.com','password',0714253669),(3,'Yassine','yass@gmail.com','password',0647586910);")
result = session.execute(sql)

sql = text ("INSERT INTO Advertisement(IdAd,AdName,AdTypePayement,AdLocalisation,AdPrice,AdDescription,IdUser,IdCar,IdCat) VALUES(1,'Porsche 718 Cayman neuve a vendre','Main Propre','Monaco',60000,'Porsche Cayman Type 987 de 2007 avec seulement 110 096 km au compteur. Cette magnifique voiture de sport est en excellent etat. Contactez moi pour plus d informations ou pour planifier un essai.',1,1,5),(2,'Tesla Model 3 de 2022 a vendre','Main Propre','Tours',43512,'a vendre  Tesla Model 3 Phase 2 de l annee 2022, avec seulement 25 882 km parcourus. Cette voiture electrique emblematique offre une conduite fluide et silencieuse. etat impeccable, aucune reparation a prevoir.Contactez-moi pour plus de details ou pour organiser un essai routier',2,2,5);")
result = session.execute(sql)

sql = text ("INSERT INTO Offers(IdOffer,OfferAcceptation,OfferPrice,IdUserAcheteur,IdUserVendeur,IdAd) VALUES (1,False,54000,2,1,1),(2,False,32000,3,2,2);")
result = session.execute(sql)

session.commit()