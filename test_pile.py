# Importation du module pile
import pile

# Création d'une nouvelle pile vide
ma_pile = pile.nouvelle_pile()

# Ajout de plusieurs éléments au sommet de la pile
pile.empiler(ma_pile, 10)  # Ajoute 10
pile.empiler(ma_pile, 11)  # Ajoute 11
pile.empiler(ma_pile, 12)  # Ajoute 12
pile.empiler(ma_pile, 13)  # Ajoute 13

# Vérifie si la pile est vide avant de retirer un élément
if not pile.pile_vide(ma_pile):
    pile.depiler(ma_pile)  # Retire l'élément au sommet (13)
else:
    print("La pile est vide, impossible de dépiler.")

# Affichage de l'état actuel de la pile
print(ma_pile)  # Affiche [10, 11, 12]
