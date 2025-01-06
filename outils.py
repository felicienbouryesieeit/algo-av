# Tableau initial
"""
tableau = [
[0, 1, 0,1],
[1, 0, 0,0],
[0, 0, 0,0],
[1, 0, 0,0]
]
"""

# Ajouter une nouvelle ligne (par exemple [10, 11, 12])



# Ajouter une nouvelle colonne (par exemple des 0 à chaque ligne)
#for ligne in tableau:
#    ligne.append(0)

# Afficher le tableau résultant
#for ligne in tableau:
    #print(ligne)



def create_tableau(tableau):
    for i in range(5):  # 0 to 4
        nouvelle_ligne = [10, 11, 12]
        tableau.append(nouvelle_ligne)
        
def compter_arretes(tableau):
    nb_arretes=0
    for i2 in range(len(tableau[0])):
        for i in range(len(tableau[i2])):

            #print(tableau[i2][i])
            
            nb_arretes+=tableau[i2][i]

    nb_arretes=nb_arretes/2
    print(nb_arretes)