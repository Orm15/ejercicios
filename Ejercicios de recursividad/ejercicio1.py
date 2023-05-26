#IMPRIMIR UNA LISTA CON RECURSIVIDAD:

s = [1,2,3,4,5]
def Imprimir(a,c = 0):
    try:
        valor = a[c]
        print(f"Dato en el indice {c} es : {valor}")
        c = c + 1
        Imprimir(a,c)
    except :
        return
    
Imprimir(s)


# print(a[c]," ")
#     if c < len(a)-1:
#         Imp(a,c+1)