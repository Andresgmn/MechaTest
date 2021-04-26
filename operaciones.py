import string

def calcTLetras(lista):

    l1 = list(string.ascii_uppercase)

    dobles = ['á', 'é', 'í', 'ó', 'ú', 'ö']

    for i in range (len(l1)):
        dobles.append(str(l1[i]))
    
    #print(dobles)
    auxiliar = 0
    numItems = 0
    #print("Esta es la lista que re recive: ", lista)
        
    for i in lista:
        for j in range (len(i)):
            if i[j] in dobles:
                auxiliar += 2
            else:
                auxiliar += 1
    #Para contar los espacio solo se cuentan el numero de palabras menos 1, por la
    #por la ultima palabra
    numItems = len(lista) - 1
    auxiliar += numItems
    #print(auxiliar)

    return auxiliar

def calculaPPM(cha,time):                                                                                                  
    ppmBase = cha / 5
    ppmCharacter = round(ppmBase, 2)
    ppmtiempo = ppmCharacter / round(time,2)
    ppm = int(ppmtiempo * 60)

    return ppm
