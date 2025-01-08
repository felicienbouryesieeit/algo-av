import outils
# Importation du module contenant des outils pour les opérations sur les graphes
from outils import parcours_en_largeur, parcours_en_profondeur, lire_graphe_format_personnalise

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

outils.compter_arcs_list_adjacente(tableau_list_adjacente)

# Lire le graphe depuis le fichier texte
matrice_adj = lire_graphe_format_personnalise()

def test_parcours_en_profondeur():
    # Point de départ pour le parcours
    sommet_depart = 3

    # Exécuter le parcours en profondeur
    resultat_obtenu = parcours_en_profondeur(matrice_adj, sommet_depart)
    print(f"Résultat du parcours en profondeur depuis le sommet {sommet_depart} :", resultat_obtenu)

# Lancer le test
test_parcours_en_profondeur()

def test_parcours_largeur():
    # Exécuter le parcours en largeur
    sommet_depart = 2
    resultat = parcours_en_largeur(matrice_adj, sommet_depart)
    print(f"Résultat du parcours en largeur depuis le sommet {sommet_depart} :", resultat)

# Lancer le test
test_parcours_largeur()



