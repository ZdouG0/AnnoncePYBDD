    RepOk=False
            while RepOk ==False:
                
                if repBack != 'Y' and repBack != 'N' and repBack != 'y' and repBack != 'n':
                    repBack = input("Entree incorrect ! Veuillez reesayer :")
                else :
                    RepOk = True
            if repBack == 'y' or repBack=='Y':
                main()