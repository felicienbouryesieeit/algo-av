# Importation du module file qui contient les fonctions de manipulation de file
import file

# Création d'une nouvelle file (initialement vide) en utilisant la fonction du module
list = file.nouvelle_file()

# Ajout de plusieurs éléments dans la file en utilisant la fonction enfiler
file.enfiler(list, 10)  # Ajoute l'élément 10
file.enfiler(list, 11)  # Ajoute l'élément 11
file.enfiler(list, 12)  # Ajoute l'élément 12
file.enfiler(list, 13)  # Ajoute l'élément 13

# Retrait du premier élément de la file en utilisant la fonction defiler
file.defiler(list)  # Supprime et retourne le premier élément (10)

# Affichage de l'état actuel de la file
print(list)  # Affiche [11, 12, 13], car 10 a été retiré
