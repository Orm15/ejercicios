#Escriba una función recursiva que verifique si una cadena es palindroma o no.


def getCad():
    cad = input()
    cadL = list(cad)
    if(contador(cadL) == 0 or contador(cadL) == 1):
        return getCad()
    else :
        return cad

def invert(palabra, numI, nc ):
    if numI  == 0 :
        return "".join(nc)
    else :
        nc.append(palabra[numI - 1])
        numI = numI - 1
        return invert(palabra,numI,nc)

def contador(a, cont = 1):
    try:
        valor = a[cont]
        cont = cont + 1
        return contador(a,cont)
    except:
        return cont


def kill():
    cad = getCad()
    cadL = list(cad)
    nc = invert(cad,contador(cadL),[])
    if cad == nc :
        print("La cadena es polindroma" )
        print(f" la cadena 1 : {cad} = cadena invertida : {nc}")
    else:
        print("Las cadenas son diferentes ")
        print(f" la cadena 1 : {cad} != cadena invertida : {nc}")

kill()