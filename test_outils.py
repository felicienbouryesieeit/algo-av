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
#p = outils.parcours_en_profondeur(2,True)
#print(p)
      
#assert outils.parcours_en_largeur(5)
#p2 = outils.parcours_en_largeur(5)
#print(p2)

#inf = outils.plus_grand_influenceur()
#print(inf)

#commu = outils.verifier_une_communautee()
#print(commu)

source = 1
destination = 5

chemin = outils.chemin_minimum(source, destination)
if chemin:
    print(f"Le chemin minimum de {source} à {destination} est : {chemin}")
else:
    print(f"Aucun chemin trouvé de {source} à {destination}.")