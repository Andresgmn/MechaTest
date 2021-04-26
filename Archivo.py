import random
import sys


def RandomSelect():
    listText = ["hobbit.txt", "llano.txt", "tiny.txt", "corto.txt"]
    return random.choice(listText)

def LeerArchivo():
    
    lista = list()
    
    selection = RandomSelect()
    with open("textos/"+selection, "r",encoding = "utf8") as f:
        lista = f.read().split()    
    return lista