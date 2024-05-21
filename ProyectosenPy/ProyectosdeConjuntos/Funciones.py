import random
def agregar():
    lista = set()
    for i in range(10):
        lista.add(random.randint(0,100))
    return lista

def Union(conj1,conj2):
    return conj1 | conj2

def intersecc(conj1,conj2):
    if(conj1.isdisjoint(conj2) == False):
        return conj1 & conj2
    else:
        return "No tiene elementos en común"
    
def Comple(conj1,conj2):
    return conj1 - conj2
