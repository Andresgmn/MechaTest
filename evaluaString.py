import string

def generaDobles():
    l1 = list(string.ascii_uppercase)
    
    dobles = ['á', 'é', 'í', 'ó', 'ú', 'ö']
    
    for i in range(len(l1)):
        dobles.append(str(l1[i]))
    return dobles

def evaluaPalabra(word, lista):
    simple = 0
    doble = 0
    
    for i in range (len(word)):
        
        if word[i] in lista:
            doble += 2
        else:
            simple += 1
    
    return simple + doble