# Escriba una función recursiva que verifica si n es primo 

def getNum():
    num = int(input())
    if num>1 :
        return num
    else : 
        return getNum()
    
def Prim(n , index, con ):
    
    if index == 1 :
        if con == 1 : return True
        else : return False
    else : 
        if n % index == 0 : 
            con = con + 1 
            return Prim(n,index - 1 ,con )
        else : 
            return Prim(n,index - 1 ,con )


def kill():
    number = getNum()
    if Prim(number, number, 0) : 
        print("El numero es primo")
    else : 
        print("El numero no es primo")

kill()