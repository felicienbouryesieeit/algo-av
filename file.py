def nouvelle_file():
    return list()

def enfiler(f, e):
    f.append(e)


def defiler(f):
    return f.pop(0)

def file(f):
    return len(f) == 0