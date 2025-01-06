import re

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

def erreur():
    # Fonction appelée pour afficher un message d'erreur générique
    print("erreur")

# Ouvre le fichier "graphe.txt" en mode lecture et lit toutes les lignes
with open("graphe.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()

# Variables globales pour suivre le nombre de sommets et le titre actuel
nb_sommet2 = 0
nb_titre_actuel = 0
nb_titre_sommet=0

def verifier_titre_global(texte1,texte2):
    global nb_titre_actuel
    #print("ok")
    chaine = texte1
    #lignes[1]
    #" SOMMETS"
    caracterenegatif=len(texte2)  # Longueur du texte attendu
    print("test : "+str(caracterenegatif))

    # Extraire la partie numérique avant le texte attendu
    nouvelle_chaine = chaine[:-caracterenegatif] 

    # Vérifie si la ligne suit le format "<nombre> texte2"
    estvalide = texte1.strip() == nouvelle_chaine.strip()+texte2 and nouvelle_chaine.strip().isdigit()
    
    # Met à jour la variable globale si valide
    if estvalide:
        nb_titre_actuel = int(nouvelle_chaine)
    return estvalide


def verifier_arretes(i):
    print("arretes"+lignes[i])
    
    pattern = r'(\w+)\s+(\w+)'

    # Recherche des deux mots
    resultat = re.findall(pattern, lignes[i])

    if (i<(len(lignes)-1)) :
    # Affichage des résultats
        print(lignes[i])
        verifier_arretes(i+1)
    else :
        print("fin du code")
    #nombre_lignes = len(lignes)
    #len(lignes)

def verifier_titre_arretes():
    verifier_arretes(nb_sommet2+2+1)


def verifier_nom_sommet(i):
        global nb_sommet2
        global nb_titre_sommet
        if verifier_titre_global(lignes[i]," ARCS")==False:
            nb_sommet2 = nb_sommet2+1
            print("sommet: "+lignes[i])
            verifier_nom_sommet(i+1)
                
        else:
            # Vérifie si le nombre de sommets correspond au titre
            print("tortue b "+str(nb_titre_sommet)+" "+str(nb_sommet2))
            if nb_titre_sommet==nb_sommet2:
                #print("tortue")
                verifier_titre_arretes()
            else : 
                erreur()  # Appelle la fonction d'erreur si les valeurs ne correspondent pas

def lire_graphe_txt():
    # Ouvrir et lire le fichier
    # Accéder à la 2e ligne (index 1)
    #nb_actuel = int(ligne_souhaitee[2])
    
    if lignes[0].strip() == "GRAPHE ORIENTE" or lignes[0].strip() == "GRAPHE NON ORIENTE":

        #print(ligne_souhaitee)  
        #isdigit()
        
        #chaine = lignes[1]

        #nouvelle_chaine = chaine[:-8]

        # Vérifie le titre global des sommets
        if verifier_titre_global(lignes[1]," SOMMETS"): #lignes[1].strip() == nouvelle_chaine.strip()+" SOMMETS" and nouvelle_chaine.strip().isdigit():
        # Vérifie le titre global des sommets
            global nb_titre_sommet
            global nb_titre_actuel

            nb_titre_sommet=nb_titre_actuel
            verifier_nom_sommet(2)  # Vérifie les noms des sommets
            #print(lignes[1])
  
        else:
            erreur()  # Appelle la fonction d'erreur si le format des sommets est incorrect
    else:
        erreur()  # Appelle la fonction d'erreur si le type de graphe est invalide

# Appelle la fonction principale pour lire et valider le fichier
lire_graphe_txt()