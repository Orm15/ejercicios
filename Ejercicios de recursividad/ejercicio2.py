#Escriba una función recursiva que encuentre el máximo común divisor de dos números enteros x,y .

num1 = int(input())
num2 = int(input())

def mcd(num1,num2):
    r = num1 % num2
    if r != 0 :
        return mcd(num2,r)
    else:
        return num2
    
print(mcd(num1,num2))