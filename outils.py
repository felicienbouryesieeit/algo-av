# Fonction pour créer et remplir un tableau avec des lignes supplémentaires
def create_tableau(tableau):
    for i in range(5):  # Boucle de 0 à 4 
        nouvelle_ligne = [10, 11, 12]  # Nouvelle ligne contenant trois éléments
        tableau.append(nouvelle_ligne)  # Ajout de la nouvelle ligne au tableau

# Fonction pour compter le nombre d'arêtes dans un graphe représenté par une matrice d'adjacence
def compter_arretes_matrice_adjacente(tableau):
    nb_arretes = 0  # Initialisation du compteur d'arêtes
    for i2 in range(len(tableau[0])):  # Parcours des colonnes de la matrice
        for i in range(len(tableau[i2])):  # Parcours des lignes de la matrice
            # Ajout de la valeur courante à la somme totale
            nb_arretes += tableau[i2][i]
    
    # Division par 2 pour éviter de compter deux fois les arêtes
    nb_arretes = nb_arretes / 2  
    print(nb_arretes)  # Affichage du nombre total d'arêtes

def compter_arcs_matrice_adjacente(tableau):
    nb_arcs = 0  # Initialisation du compteur d'arcs
    for i2 in range(len(tableau[0])):  # Parcours des colonnes de la matrice
        for i in range(len(tableau[i2])):  # Parcours des lignes de la matrice
            # Ajout de la valeur courante à la somme totale
            nb_arcs += tableau[i2][i]
    
    print(nb_arcs)  # Affichage du nombre total d'arc

# Fonction pour compter le nombre d'arêtes dans un graphe représenté par une liste d'adjacence
def compter_arretes_list_adjacente(tableau):
    nb_sommets_visites = set()  # Ensemble pour éviter de compter deux fois les mêmes arêtes
    nb_arretes = 0  # Initialisation du compteur d'arêtes

    for sommet, voisins in tableau.items():
        for voisin in voisins:
            # Vérification si l'arête a déjà été comptée dans les deux sens
            if (sommet, voisin) not in nb_sommets_visites and (voisin, sommet) not in nb_sommets_visites:
                nb_sommets_visites.add((sommet, voisin))  # Ajout de l'arête à l'ensemble
                nb_arretes += 1  # Incrémentation du compteur d'arêtes

    print(nb_arretes)  # Affichage du nombre total d'arêtes

def compter_arcs_list_adjacente(liste_adjacence):
    nb_arcs = 0

    for sommet, voisins in liste_adjacence.items():
        nb_arcs += len(voisins)  # Chaque voisin représente un arc sortant

    print(nb_arcs)

