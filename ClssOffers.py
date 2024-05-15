from createdatabase import *

class COffers :

    def __init___(self,Etat,Prix,Acheteur,Vendeur,Annonce):
        offer=Offers(OfferAcceptation=Etat,OfferPrice=Prix,IdUserAcheteur=Acheteur,IdUserVendeur=Vendeur,IdAd=Annonce)
        session.add(offer)
        session.commit()




