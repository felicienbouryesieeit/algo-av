# Création d'une nouvelle file
def nouvelle_file():
    return list()

# Ajout d'un élément à la fin de la file
def enfiler(f, e):
    f.append(e)

# Retrait du premier élément de la file
# Assurez-vous que la file n'est pas vide avant d'appeler cette fonction
def defiler(f):
    return f.pop(0)

# Vérifie si la file est vide
def estvide(f):
    return len(f) == 0
