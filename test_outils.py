import outils

# Définition d'une matrice d'adjacence pour un graphe
# Chaque ligne/colonne représente un nœud, et une valeur de 1 indique une arête entre les nœuds correspondants
tableau_matrice_adjacente = [
    [0, 1, 1, 1],  # Le premier nœud est connecté aux trois autres
    [1, 0, 0, 0],  # Le deuxième nœud est connecté uniquement au premier
    [1, 0, 0, 0],  # Le troisième nœud est connecté uniquement au premier
    [1, 0, 0, 0]   # Le quatrième nœud est connecté uniquement au premier
]

# Définition d'une liste d'adjacence pour un graphe
# Chaque clé représente un nœud, et la valeur est une liste de nœuds auxquels il est connecté
tableau_list_adjacente = {
    "Aurora": ["Olavi", "Tapio"],  # "Aurora" est connecté à "Olavi" et "Tapio"
    "Ilona": [],                   # "Ilona" n'a aucune connexion
    "Olavi": ["Aurora"],           # "Olavi" est connecté uniquement à "Aurora"
    "Tapio": ["Aurora"]            # "Tapio" est connecté uniquement à "Aurora"
}

# Appel d'une fonction pour compter le nombre d'arêtes dans le graphe représenté par la matrice d'adjacence
outils.compter_aretes_matrice_adjacente(tableau_matrice_adjacente)

outils.compter_arcs_matrice_adjacente(tableau_matrice_adjacente)

# Appel d'une fonction pour compter le nombre d'arêtes dans le graphe représenté par la liste d'adjacence
outils.compter_aretes_list_adjacente(tableau_list_adjacente)

# Compte le nombre d'arcs dans le graphe représenté par la liste d'adjacence
outils.compter_arcs_list_adjacente(tableau_list_adjacente)

# Effectue un parcours en profondeur (Depth-First Search) à partir du nœud 0 (dans un graphe représenté en interne)
p = outils.parcours_en_profondeur(8, True)
print(f"\nLe parcour en profondeur est : " + str(p))

p2 = outils.parcours_en_largeur(8, False,True)
print(f"\nLe parcour en largeur est : " + str(p2))

inf = outils.plus_grand_influenceur()
print(f"\nLe plus grand influenceur est : " + str(inf))

commu = outils.verifier_une_communautee()
print(f"\nLa communautée est : " + str(commu))

prop = outils.propagation(0,1)
dur = outils.temps_de_propagation(0,1)

print(f"\nChemin le plus cours : " + str(prop))

print(f"\nDurée: "+str(dur)+" minutes ")