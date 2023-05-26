val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
}


def RomanToNatural(cade,cont,present,prev,sum):
    if cont == 0:
        return sum
    else :
        present = val[cade[cont-1].upper()]
        if present >= prev :
            sum = sum + present
        else :
            sum = sum - present
        cont = cont - 1
        return RomanToNatural(cade,cont,present,present,sum)
        
def kill():
    cade = input()
    print(f" El valor en natural es: {RomanToNatural(cade,len(cade),0,0,0)}")

kill()


 
        


