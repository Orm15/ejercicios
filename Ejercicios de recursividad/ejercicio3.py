#Escriba una función recursiva que imprima en pantalla los números desde n a 0	
def Valor():
    n = int(input())
    if n < 1:
        return Valor()
    return n

def imp(num):
    if num >= 0:
        print(num)
        imp(num - 1)

imp(Valor())
