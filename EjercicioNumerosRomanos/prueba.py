s = "avion"
cont = 0
for i in s :
    try : 
        print(i+f"  next: {s[cont + 1]}")
        cont = cont + 1
    except IndexError:
        print("la cadena se acabo")