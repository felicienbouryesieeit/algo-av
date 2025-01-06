def nouvelle_pile():
    return list()

def emplier(p, e):
    p.append(e)

def depiler(p):
    return p.pop()

def pile_vide(p):
    return len(p) == 0