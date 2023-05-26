#Cree una función recursiva que dada una lista cuenta la cantidad de elementos que son impares.
#Cree una función recursiva que dada una lista cuenta la cantidad de elementos con números primos.


def co(are, conP = 0, conI = 0,con = 0):
    try :
        index = are[con]
        if are[con] % 2 == 1 :
            conI = conI + 1
        if primo(are[con]):
            conP = conP + 1
        con = con + 1
        return co(are,conP,conI,con)
    except IndexError : 
        return conP,conI

def primo(n, cont = 0 , div = 2):
    if div >= n:
        if cont == 0 :
            return True
        else :
            return False
    else :
        if n % div == 0 :
            cont = cont + 1
            div = div + 1
            return primo(n,cont,div)
        else :
            div = div + 1
            return primo(n,cont,div)


def kill():
    a = [1, 2, 3, 4, 5]
    prim , imp = co(a)
    print(f" Tiene {prim} numeros primos y {imp} numeros impares")

kill()