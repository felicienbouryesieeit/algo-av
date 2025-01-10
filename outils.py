import re
import pile
import file

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

def erreur(message="\nErreur : Format ou données invalides"):
    # Fonction appelée pour afficher un message d'erreur générique
    print(message)

# Ouvre le fichier "graphe.txt" en mode lecture et lit toutes les lignes
#with open("graphe.txt", "r", encoding="utf-8") as fichier:

with open("graphe.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()


# Variables globales pour suivre le nombre de sommets et le titre actuel
nb_sommet2 = 0
nb_arcs2 = 0
nb_titre_actuel = 0
nb_titre_sommet = 0
basenumero = 0

som = []
somint=[]
adj = []
adjint=[]
mat = []
visite = []
som_visites=[]
som_visites2=[]

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

def verifier_titre_global(texte1,texte2):
    global nb_titre_actuel
    chaine = texte1
    caracterenegatif = len(texte2)  # Longueur du texte attendu

    # Extraire la partie numérique avant le texte attendu
    nouvelle_chaine = chaine[:-caracterenegatif] 

    # Vérifie si la ligne suit le format "<nombre> texte2"
    estvalide = (texte1.strip() == nouvelle_chaine.strip()+texte2 and nouvelle_chaine.strip().isdigit())
    
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
            
def verifier_aretes(i):
    global nb_arcs2
    
    pattern = r'(\w+)\s+(\w+)'
    nb_arcs2 += 1
    # Recherche des deux mots
    resultat = re.findall(pattern, lignes[i])
    #print(f"\naretes "+resultat[0][1])
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
            #print(f"sommet: "+str(somint[len(somint)-1]))
            verifier_nom_sommet(i+1)
                
        else:
            # Vérifie si le nombre de sommets correspond au titre
            if nb_titre_sommet == nb_sommet2:
                verifier_titre_aretes()
            else : 
                print(f"\nLe nombre de sommets ne correspond pas : {nb_sommet2}/{nb_titre_sommet}") # Appelle la fonction d'erreur si les valeurs ne correspondent pas


# Crée une matrice d'adjacence initialisée à 0
def creer_matrice():
    try:
        print("Som est : " + str(len(som)))  # Affiche la taille de la liste 'som'
        global mat
        matrice = []

        # Boucle pour initialiser la matrice avec des zéros
        for i in range(len(som)):
            matrice2 = []
            for j in range(len(som)):
                matrice2.append(0)
            matrice.append(matrice2)
        
        mat = matrice
        rajouter_les_arcs()
    except NameError as e:
        print(f"Erreur : une variable globale nécessaire n'est pas définie ({e}).")
    except Exception as e:
        print(f"Erreur inattendue lors de la création de la matrice : {e}")

# Ajoute les arcs à la matrice d'adjacence
def rajouter_les_arcs():
    try:
        global mat
        global visite

        # Parcourt la liste des arcs et met à jour la matrice
        for i in range(len(adjint)):
            mat[adjint[i][visite[0]]][adjint[i][visite[1]]] = 1

        # Affiche la matrice avec les sommets
        for i in range(len(mat)):
            print(str(som[i]).strip() + " " + str(mat[i]))
    except IndexError as e:
        print(f"Erreur d'indice lors de l'ajout des arcs : {e}")
    except NameError as e:
        print(f"Erreur : une variable globale nécessaire n'est pas définie ({e}).")
    except Exception as e:
        print(f"Erreur inattendue lors de l'ajout des arcs : {e}")

# Initialise les données pour le graphe et détermine l'ordre des visites
def begin_graphe(visite2):
    try:
        global visite
        # Définit l'ordre des visites en fonction du paramètre
        if visite2:
            visite = [0, 1]
        else:
            visite = [1, 0]
        
        lire_graphe_txt()  # Appelle une fonction externe pour lire le graphe
    except NameError as e:
        print(f"Erreur : une variable globale ou fonction nécessaire n'est pas définie ({e}).")
    except Exception as e:
        print(f"Erreur inattendue dans 'begin_graphe' : {e}")

def voisins (depart):
    global mat

    list_voisins = []


    for x in range(len(mat[depart])) :

        if mat[depart][x] == 1 :
            list_voisins.append(x)
    

    return list_voisins

def parcours_en_profondeur(depart,havebegingraphe):
    if havebegingraphe == True:
        begin_graphe(True)
    
    global mat
    res = file.nouvelle_file()
    av = pile.nouvelle_pile()
    vu = set()

    pile.empiler(av, depart)
    while not pile.estvide(av):
        cand = pile.depiler(av)

        if not cand in vu :
            vu.add(cand)
            file.emfiler(res, cand)
            for v in voisins(cand):
                pile.empiler(av, v)
    return res

def parcours_en_largeur(depart,chercheunnombre):
    begin_graphe(True)
    global mat
    global chemin_de_propagation
    global chemin_de_propagation2
    global destination
    global destination_global
    
    chemin_de_propagation2=[-1,-1,-1]

    res = file.nouvelle_file()
    av = file.nouvelle_file()
    vu = set()

    vu.add(depart)
    file.emfiler(av, depart)

    nombre_a_ete_trouve=False

    while not file.estvide(av):
        cand = file.defiler(av)
        res.append(cand)

        voisinsliste=voisins(cand)
        
        
        

        if (chercheunnombre==True) and (nombre_a_ete_trouve==False) :
            
            
            chemin_de_propagation3 = []

            chemin_de_propagation2[0]=cand
            print("base : "+str(cand))

            for voisin in voisinsliste:
                voisinsliste2 = voisins(voisin)
                print("resultat1 : "+str(voisinsliste))
                if (voisin==destination) :
                    chemin_de_propagation2[1]=destination
                    nombre_a_ete_trouve=True

                    
                    chemin_de_propagation3.append(voisin)

                for voisin2 in voisinsliste2:
                    print("resultat 2 :"+ str(voisinsliste2))
                    if  (voisin2==destination) and (chemin_de_propagation2[1]==-1) :

                        
                        
                        chemin_de_propagation3.append(voisin)
                        chemin_de_propagation3.append(voisin2)

                        nombre_a_ete_trouve=True

                if voisin not in vu:
                    vu.add(voisin)
                    file.emfiler(av, voisin)
    if (nombre_a_ete_trouve==True) :

        

        chemin_de_propagation2_debut=chemin_de_propagation2[0]
        destination=chemin_de_propagation2_debut

        #chemin_de_propagation.pop(0)

        

        #chemin_de_propagation3= chemin_de_propagation3 + chemin_de_propagation

        #chemin_de_propagation3.pop()


        chemin_de_propagation = chemin_de_propagation3 + chemin_de_propagation 

        chemin_de_propagation4=[]
        limite_propagation=False
    
        for a in chemin_de_propagation:
            
            
            if limite_propagation==False:
                chemin_de_propagation4.append(a)
            
            if (a==destination_global):
                limite_propagation=True
        
        
        chemin_de_propagation=chemin_de_propagation4
        

        if (chemin_de_propagation2_debut!=depart) :
            parcours_en_largeur(depart,True)
        else : 
            chemin_de_propagation4=chemin_de_propagation
            chemin_de_propagation=[]
            chemin_de_propagation.append(depart)
            chemin_de_propagation=chemin_de_propagation+chemin_de_propagation4


    return res

def verifier_une_communautee():
    global somint
    begin_graphe(True)
    une_communaute=False
    for i in range(len(somint)):
        res = parcours_en_profondeur(i, False)
        if (len(res)==len(somint)) : 
            une_communaute=True
        return une_communaute
        
def plus_grand_influenceur() : 
    global mat
    plus_grand_influenceur_liens_int = 0
    plus_grand_influenceur_int=0
    begin_graphe(True)
    for i in range(len(mat)):
        current_influenceur=0
        for i2 in range(len(mat)):
            current_influenceur= current_influenceur + mat[i][i2]
        if current_influenceur>plus_grand_influenceur_liens_int:
            plus_grand_influenceur_liens_int=current_influenceur
            plus_grand_influenceur_int=i
    return plus_grand_influenceur_int



#res2 = parcours_en_largeur(0,False)
#print(res2)


chemin_de_propagation=[]
chemin_de_propagation2=[]
destination=0
destination_global=0
def propagation(depart,destination2):
    global chemin_de_propagation
    global chemin_de_propagation2
    global destination
    global destination_global
    destination=destination2
    destination_global=destination
    chemin_de_propagation=[]
    #print("chien"+str(chemin_de_propagation2[2]))
    parcours_en_largeur(depart,True)
    return chemin_de_propagation




def temps_de_propagation(depart,destination2):
    chemin = propagation(  depart,destination2)
    durée=(len(chemin)-1)*5
    return durée

#toto = temps_de_propagation(0,2)
#print("temps de propagation "+str(toto))