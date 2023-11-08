print("""Bonjour!
      Voila notre offres d abonnement""")
print("============================================================================")
T=[
    [200,float("inf"),0],
    [100,120,0.5],
    [50,60,1],
    [20,30,1.5],
    [0,0,2],
]

for i in range(5):
    print(f"Abonnement mensuel:{T[i][0]}",f" Minutes Gratuits:{T[i][1]}",f" Cout la minute:{T[i][2]}Dh")
choix=True
while choix:
    print(""" 
            1 - Restart le programme 
            2 - Afficher la liste du coût mensuel par offre
            3 - Afficher l'offre la plus intéressante (moindre coût)
            4 - Quitter le programme
            """)
    choix=int(input("entrer votre choix:"))
    if choix==2:
        duree=input("Sasire la duree de communication en minutes:")
        if duree.isdigit()==False:
             print("Veuillez d'abord entrer un nombre pour la durée de communication.")
        else:
            duree=int(duree)
            T1=[]
            for i in range(5):
                if duree>T[i][1]:
                    price=( ( ( duree - T[i][1] ) * T[i][2] ) + T[i][0] )
                else :
                    price = T[i][0]
                T1.append(price)
                print(f"L'ofrre de {T[i][0]} DH est :",T1[i],"DH")
    elif choix==3:
        for i in range(5):
            s=min(T1)-(duree - T[i][1] )*T[i][2]
            if s == T[i][0]:
                of=T[i][0]
        print(f"l offre le plus interesant est le plan de {of} Dh")   
    elif choix == 4 :
        print("\nAu revoir!")
        choix = None
        
            
                

