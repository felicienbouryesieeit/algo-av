import re

# Fonction pour créer et remplir un tableau avec des lignes supplémentaires
def create_tableau(tableau):
    for i in range(5):  # Boucle de 0 à 4 
        nouvelle_ligne = [10, 11, 12]  # Nouvelle ligne contenant trois éléments
        tableau.append(nouvelle_ligne)  # Ajout de la nouvelle ligne au tableau

# Fonction pour compter le nombre d'arêtes dans un graphe représenté par une matrice d'adjacence
def compter_aretes_matrice_adjacente(tableau):
    nb_aretes = 0  # Initialisation du compteur d'arêtes
    for j in range(len(tableau[0])):  # Parcours des colonnes de la matrice
        for i in range(len(tableau[j])):  # Parcours des lignes de la matrice
            # Ajout de la valeur courante à la somme totale
            nb_aretes += tableau[j][i]
    
    # Division par 2 pour éviter de compter deux fois les arêtes
    nb_aretes = nb_aretes / 2  
    print(nb_aretes)  # Affichage du nombre total d'arêtes

def compter_arcs_matrice_adjacente(tableau):
    nb_arcs = 0  # Initialisation du compteur d'arcs
    for j in range(len(tableau[0])):  # Parcours des colonnes de la matrice
        for i in range(len(tableau[j])):  # Parcours des lignes de la matrice
            # Ajout de la valeur courante à la somme totale
            nb_arcs += tableau[j][i]
    
    print(nb_arcs)  # Affichage du nombre total d'arc

# Fonction pour compter le nombre d'arêtes dans un graphe représenté par une liste d'adjacence
def compter_aretes_list_adjacente(tableau):
    nb_sommets_visites = set()  # Ensemble pour éviter de compter deux fois les mêmes arêtes
    nb_aretes = 0  # Initialisation du compteur d'arêtes

    for sommet, voisins in tableau.items():
        for voisin in voisins:
            # Vérification si l'arête a déjà été comptée dans les deux sens
            if (sommet, voisin) not in nb_sommets_visites and (voisin, sommet) not in nb_sommets_visites:
                nb_sommets_visites.add((sommet, voisin))  # Ajout de l'arête à l'ensemble
                nb_aretes += 1  # Incrémentation du compteur d'arêtes

    print(nb_aretes)  # Affichage du nombre total d'arêtes

def compter_arcs_list_adjacente(liste_adjacence):
    nb_arcs = 0

    for sommet, voisins in liste_adjacence.items():
        nb_arcs += len(voisins)  # Chaque voisin représente un arc sortant

    print(nb_arcs)



# Variables globales pour suivre le nombre de sommets et le titre actuel
nb_sommet2 = 0
nb_arcs2=0
nb_titre_actuel = 0
nb_titre_sommet=0

som = []
somint=[]
adj = []
adjint=[]
mat = []
visite = []

def erreur(message="\nErreur : Format ou données invalides"):
    # Fonction appelée pour afficher un message d'erreur générique
    print(message)

# Ouvre le fichier "graphe.txt" en mode lecture et lit toutes les lignes
def lire_graphe_format_personnalise():
    with open("graphe.txt", "r", encoding="utf-8") as fichier:
        lignes = [ligne.strip() for ligne in fichier.readlines()]

    # Vérification du type de graphe
    if lignes[0] != "GRAPHE ORIENTE":
        raise ValueError("Le fichier doit commencer par 'GRAPHE ORIENTE'.")

    # Lecture du nombre de sommets
    try:
        nb_sommets = int(lignes[1].split()[0])
    except ValueError:
        raise ValueError("La seconde ligne doit contenir '<nombre> SOMMETS'.")

    # Vérification et lecture des sommets
    sommets = []
    for i in range(2, 2 + nb_sommets):
        sommets.append(int(lignes[i]))
    if len(sommets) != nb_sommets:
        raise ValueError("Le nombre de sommets ne correspond pas à l'en-tête.")

    # Lecture du nombre d'arcs
    arcs_ligne = 2 + nb_sommets
    try:
        nb_arcs = int(lignes[arcs_ligne].split()[0])
    except ValueError:
        raise ValueError("La ligne après les sommets doit contenir '<nombre> ARCS'.")

    # Lecture des arcs
    arcs = []
    for i in range(arcs_ligne + 1, arcs_ligne + 1 + nb_arcs):
        sommet1, sommet2 = map(int, lignes[i].split())
        arcs.append((sommet1, sommet2))

    # Construction de la matrice d'adjacence
    matrice_adj = [[0 for _ in range(nb_sommets)] for _ in range(nb_sommets)]
    for sommet1, sommet2 in arcs:
        matrice_adj[sommet1][sommet2] = 1  # Ajouter un arc orienté

    return matrice_adj
        
def verifier_titre_global(texte1,texte2):
    global nb_titre_actuel
    chaine = texte1
    caracterenegatif = len(texte2)  # Longueur du texte attendu

    # Extraire la partie numérique avant le texte attendu
    nouvelle_chaine = chaine[:-caracterenegatif] 

    # Vérifie si la ligne suit le format "<nombre> texte2"
    estvalide = texte1.strip() == nouvelle_chaine.strip()+texte2 and nouvelle_chaine.strip().isdigit()
    
    # Met à jour la variable globale si valide
    if estvalide:
        nb_titre_actuel = int(nouvelle_chaine)
    return estvalide

def ajouter_adjint(resultat):
    adjint_actuel=[ajouter_adjint2(resultat,0),ajouter_adjint2(resultat,1)]
    print("adjint actuel : "+str(adjint_actuel))
    adjint.append(adjint_actuel)

def ajouter_adjint2(resultat,index):
    
    arc1=0
    for j in range(len(som)):
        if str(som[j]).strip() == str(resultat[0][index]).strip():
            arc1 = j
            
    return arc1

def creer_matrice():
    print("Som est : "+str(len(som)))
    global mat
    matrice = []
    for i in range(len(som)):
        
        matrice2=[]
        
        for j in range(len(som)):
            matrice2.append(0)
            
        matrice.append(matrice2)
    mat = matrice
    rajouter_les_arcs()

def rajouter_les_arcs():
    global mat
    global visite

    for i in range(len(adjint)):
        sommet1 = adjint[i][visite[0]]
        sommet2 = adjint[i][visite[1]]
        if sommet1 >= len(mat) or sommet2 >= len(mat):
            print(f"Erreur : sommet hors limites ({sommet1}, {sommet2})")
            continue
        mat[sommet1][sommet2] = 1  # Ajouter l'arc

    print("Matrice après ajout des arcs :")
    for ligne in mat:
        print(ligne)

# Appelle la fonction principale pour lire et valider le fichier
def begin_graphe(visite2):
    global visite
    if visite2:
        visite = [0,1]
    else :
        visite = [1,0]
    
    lire_graphe_format_personnalise()

def parcours_en_profondeur(matrice_adj, sommet_depart):
    def explorer_sommet(sommet, visites):
        visites.add(sommet)           # Marque le sommet actuel comme visité
        resultat.append(sommet)       # Ajoute le sommet au résultat
        for voisin, est_adjacent in enumerate(matrice_adj[sommet]):
            # Si le voisin est adjacent et non encore visité, on le visite
            if est_adjacent == 1 and voisin not in visites:
                explorer_sommet(voisin, visites)

    resultat = []                     # Liste pour stocker les sommets visités
    visites = set()                   # Ensemble des sommets déjà visités

    # Lancement du parcours (aucune vérification préalable du sommet ou de la matrice)
    explorer_sommet(sommet_depart, visites)

    return resultat                   # Retourne la liste des sommets visités

def parcours_en_largeur(matrice_adj, sommet_depart):
    # Initialisation des variables :
    # 'visites' pour conserver l'ordre des sommets visités
    # 'file' pour représenter une file d'attente des sommets à visiter
    # 'deja_visites' pour éviter de visiter plusieurs fois le même sommet
    visites = []              # Liste des sommets visités dans l'ordre
    file = [sommet_depart]    # File d'attente des sommets à explorer
    deja_visites = set()      # Ensemble des sommets déjà visités

    # Parcours en largeur
    while file:
        # Récupère le premier sommet de la file
        sommet = file.pop(0)

        # Vérifie si le sommet n'a pas encore été visité
        if sommet not in deja_visites:
            visites.append(sommet)       # Ajoute le sommet à la liste des visites
            deja_visites.add(sommet)     # Marque le sommet comme visité

            # Parcourt les voisins du sommet
            for voisin, est_adjacent in enumerate(matrice_adj[sommet]):
                # Si le voisin est adjacent et non encore visité, on l'ajoute à la file
                if est_adjacent == 1 and voisin not in deja_visites:
                    file.append(voisin)

    return visites

