def traitement_choix ():
    print ("\n===Que souhaitez-vous boire?===")
    print ("1- Café")
    print ("2- Thé")
    print ("3- Eau chaude")
    print ("4- Quitter Menu") 

def gerer_choix():
    commandes = []
    while True :
        traitement_choix()
        choix = input ("Faites votre choix :")
        if choix == "1":
            print ("Vous avez choisi un café ☕")
            commandes.append ("Café")
        elif choix == "2":
            print ("Vous avez choisi le thé 🍵")
            commandes.append ("Thé")
        elif choix == "3":
            print ("Vous avez choisi l'eau chaude 🥛")
            commandes.append ("Eau chaude")
        elif choix == "4":
            print ("Vous avez quitter le menu")
            break
        else:
            print ("❌ Votre choix n'est pas repertorié")

    print("\n🧾 Votre commande :")
    if commandes:
        compteur = {}
        pluriel= {
            "Café": "Cafés",
            "Thé": "Thés",
            "Eau chaude": "Eaux chaudes"
        }
        for boisson in commandes:
            if boisson in compteur:
                compteur[boisson] += 1
            else:
                compteur[boisson] = 1

        for boisson, nombre in compteur.items():
            nom_boisson= boisson if nombre == 1 else pluriel.get (boisson , boisson + "s")
            print (f"{nombre} {nom_boisson}")
    else:
        print("Aucune boisson n'a été commandée.")
         






