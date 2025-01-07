
# Crée une nouvelle pile
def nouvelle_pile():
    return list()

# Ajoute un élément au sommet de la pile
def empiler(p, e):
    p.append(e)

# Retire et retourne l'élément au sommet de la pile
# Assurez-vous que la pile n'est pas vide avant d'appeler cette fonction
def depiler(p):
    return p.pop()

# Vérifie si la pile est vide
def pile_vide(p):
    return len(p) == 0

