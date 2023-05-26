#Cree una función recursiva que dada una lista cuenta la cantidad de elementos

def co(are, con=0):
    try :
        index = are[con]
        return co(are, con + 1)
    except IndexError : 
        return con

def kill():
    a = [1, 2, 3, 4, 5]
    print(f" The list has {co(a)} elements")

kill()


