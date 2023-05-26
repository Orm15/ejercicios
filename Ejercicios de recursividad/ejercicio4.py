#Escriba una función recursiva que  dada una cadena retorna la inversa de la misma.

def getCadent():
    cad = input()
    s = list(cad)
    if len(s) == 0 or len(s) == 1:
        return getCadent()
    else : 
        return s

def inverted(l, indices, invertible):

    if indices >= 0:
        invertible.append(l[indices])
        return inverted(l, indices - 1, invertible)
    else:
        return "".join(invertible)

def eje():
    s = getCadent()
    cad = inverted(s, len(s) - 1, [])
    print(f"the  invert string is: {cad}")

eje()

