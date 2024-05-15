while FiltreOk ==False:
    
    if repfiltre != 'Y' and repfiltre != 'N' and repfiltre != 'y' and repfiltre != 'n':
        repfiltre = input("Entree incorrect ! Veuillez reesayer :")
    else :
        FiltreOk = True
if repfiltre == 'y' or repfiltre=='Y':
    print("Veuillez choisir vos filtres :")
