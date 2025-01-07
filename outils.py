import re

# Fonction pour créer et remplir un tableau avec des lignes supplémentaires
def create_tableau(tableau):
    for i in range(5):  # Boucle de 0 à 4 
        nouvelle_ligne = [10, 11, 12]  # Nouvelle ligne contenant trois éléments
        tableau.append(nouvelle_ligne)  # Ajout de la nouvelle ligne au tableau

# Fonction pour compter le nombre d'arêtes dans un graphe représenté par une matrice d'adjacence
def compter_aretes_matrice_adjacente(tableau):
    nb_aretes = 0  # Initialisation du compteur d'arêtes
    for i2 in range(len(tableau[0])):  # Parcours des colonnes de la matrice
        for i in range(len(tableau[i2])):  # Parcours des lignes de la matrice
            # Ajout de la valeur courante à la somme totale
            nb_aretes += tableau[i2][i]
    
    # Division par 2 pour éviter de compter deux fois les arêtes
    nb_aretes = nb_aretes / 2  
    print(nb_aretes)  # Affichage du nombre total d'arêtes

def compter_arcs_matrice_adjacente(tableau):
    nb_arcs = 0  # Initialisation du compteur d'arcs
    for i2 in range(len(tableau[0])):  # Parcours des colonnes de la matrice
        for i in range(len(tableau[i2])):  # Parcours des lignes de la matrice
            # Ajout de la valeur courante à la somme totale
            nb_arcs += tableau[i2][i]
    
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

def erreur(message="\nErreur : Format ou données invalides"):
    # Fonction appelée pour afficher un message d'erreur générique
    print(message)

# Ouvre le fichier "graphe.txt" en mode lecture et lit toutes les lignes
#with open("graphe.txt", "r", encoding="utf-8") as fichier:
with open(r"algo-av/graphe.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()


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
#print ("liste sommet " + str(tuple(liste_sommet)))

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
        #if str(resultat[i2][0]).strip() == str(som[i2]).strip():
        #print("c est bon : "+str(str(som[i2]).strip() == str(resultat[0][0]).strip()))
    print("adjint actuel : "+str(adjint_actuel))
    adjint.append(adjint_actuel)

def ajouter_adjint2(resultat,index):
    
    arc1=0
    for i2 in range(len(som)):
        if str(som[i2]).strip() == str(resultat[0][index]).strip():
            arc1 = i2
            
    return arc1
            
def verifier_aretes(i):
    global nb_arcs2
    
    pattern = r'(\w+)\s+(\w+)'
    nb_arcs2 += 1
    # Recherche des deux mots
    resultat = re.findall(pattern, lignes[i])
    print(f"\naretes "+resultat[0][1])
    adj.append(resultat)
    ajouter_adjint(resultat)

    if (i<(len(lignes)-1)) :
    # Affichage des résultats
        verifier_aretes(i+1)
    else :
        if nb_titre_actuel==nb_arcs2:
            print(f"\nValidation des arêtes réussie : {nb_arcs2}/{nb_titre_actuel}")
            creer_matrice()
        else :
            erreur(f"\nLe nombre d'arêtes ne correspond pas : {nb_arcs2}/{nb_titre_actuel}")
        
def verifier_titre_aretes():
    global nb_arcs2
    nb_arcs2 = 0
    verifier_aretes(nb_sommet2+2+1)
    
def verifier_nom_sommet(i):
        global nb_sommet2
        global nb_titre_sommet
        if verifier_titre_global(lignes[i]," ARCS") == False:
            nb_sommet2 = nb_sommet2+1
            som.append(lignes[i]) 
            somint.append(i-2)
            print(f"sommet: "+str(somint[len(somint)-1]))
            verifier_nom_sommet(i+1)
                
        else:
            # Vérifie si le nombre de sommets correspond au titre
            if nb_titre_sommet == nb_sommet2:
                verifier_titre_aretes()
            else : 
                erreur(f"\nLe nombre de sommets ne correspond pas : {nb_sommet2}/{nb_titre_sommet}") # Appelle la fonction d'erreur si les valeurs ne correspondent pas

def lire_graphe_txt():
    # Ouvrir et lire le fichier    
    if lignes[0].strip() == "GRAPHE ORIENTE" or lignes[0].strip() == "GRAPHE NON ORIENTE":

        # Vérifie le titre global des sommets
        if verifier_titre_global(lignes[1]," SOMMETS"): #lignes[1].strip() == nouvelle_chaine.strip()+" SOMMETS" and nouvelle_chaine.strip().isdigit():
        # Vérifie le titre global des sommets
            global nb_titre_sommet
            global nb_titre_actuel

            nb_titre_sommet=nb_titre_actuel
            verifier_nom_sommet(2)  # Vérifie les noms des sommets  
        else:
            erreur(f"\nFormat du titre des sommets invalide.") # Appelle la fonction d'erreur si le format des sommets est incorrect
    else:
        erreur(f"\nLe type de graphe est invalide.") # Appelle la fonction d'erreur si le type de graphe est invalide

def creer_matrice():
    print("Som est : "+str(len(som)))
    global mat
    matrice = []
    for i in range(len(som)):
        
        matrice2=[]
        
        for i2 in range(len(som)):
            matrice2.append(0)
            
        matrice.append(matrice2)
    #print(matrice)
    mat = matrice
    rajouter_les_arcs()

def rajouter_les_arcs():
    global mat
    print("oui")
    #for i2 in range(len(som)):
    #    if str(adj[i][0][0]).strip() == str(som[i2]).strip():
    #            print((adj[i][0][0]).strip())

    for i in range(len(adjint)):
        print("jsp")
        mat[adjint[i][0]][adjint[i][1]]=1
    
    # mat[1][2]=42
    
    for i in range(len(mat)):
        print(str(som[i]).strip()+" "+str(mat[i]))

# Appelle la fonction principale pour lire et valider le fichier
lire_graphe_txt()