def main():
    choix = True
    allOffers = None
    while choix:
        print('-----------------------------------------')
        print(""" 
        0 - Restart
        1 - Afficher la liste du coût mensuel par offre
        2 - Afficher l'offre la plus intéressante (moindre coût)
        3 - Quitter le programme
        """)
        print('-----------------------------------------')

        choix = input("Entrez votre choix : ")
        if choix == "1":
            dureeCom = input("Entrez la durée de communication : ")
            if not dureeCom.isdigit():
                print("Veuillez d'abord entrer un nombre pour la durée de communication.")
            else:
                dureeCom = int(dureeCom)
                allOffers = calculeOffer(dureeCom)
                print("La liste des offres avec leurs coûts :")
                print('-----------------------------------------')
                for offer in allOffers:
                    print(f"{offer['name']}: {offer['cost']} DH")               
        elif choix == "2":
            if allOffers is not None:
                print("L'offre la plus intéressante est:", allOffers[0]["name"])
            else:
                print("Veuillez d'abord afficher la liste des coûts mensuels par offre (choix 1).")
        elif choix == "3":
            print("\nAu revoir")
            choix = None
        elif choix == "0":
            choix = True
        else:
            print("\nChoix invalide, veuillez réessayer!")

def calculCout(duree, cout):
    return duree * cout

def calculeOffer(duree):
    offers = [
        {"name": "PLAN 100DH", "price": 100.00, "free": 120, "cost": 0.5},
        {"name": "PLAN 50DH", "price": 50.00, "free": 60, "cost": 1.0},
        {"name": "PLAN 20DH", "price":20.00, "free": 30, "cost": 1.5},
        {"name": "PLAN 0DH", "price":0.00,"free": 0, "cost": 2.0},
    ]

    best_offer = {"name": "PLAN 200DH",  "price": 200, "free": float('inf'), "cost": 200}

    for offer in offers:
        if duree >= offer["free"]:
            offer["cost"] =  (calculCout(duree - offer["free"], offer["cost"]) + offer["price"])

    if duree >= best_offer["free"]:
        best_offer["cost"] =  calculCout(duree - best_offer["free"], best_offer["cost"])

    offers.append(best_offer)
    def get_offer_cost(offer):
        return offer["cost"]

    offers = sorted(offers, key=get_offer_cost)

    return offers

main()