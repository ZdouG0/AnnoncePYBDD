from sqlalchemy import create_engine, Column,Integer,String
from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine("mysql+mysqlconnector://root:password@127.0.0.1/voiturebdd", echo= None)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session= Session()

#Definition de la Table Users

class Users(Base) :
    __tablename__ = 'Users'

    IdUser = Column(Integer,primary_key=True)
    UserName = Column(String(50))
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
    AdDescription = Column(String(500))
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