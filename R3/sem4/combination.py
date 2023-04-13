print("\n Bienvenido a la calculadora de combinaciones.")
def factorial (entero):
    if entero != 0:
        f = 1
        for i in range(1, entero+1):
            f *=i
        return f
    else: return(1)


n = int(input("Ingrese la el total de objetos a combinar: "))
r = int(input("Ingrese la el tamaño del grupo muestra: "))
nF = factorial(n)
rF = factorial(r)
nMrF = factorial(n-r)

#for i in range(1, n+1):
#    nF *= i
#
#for j in range(1, r+1):
#    rF *= j
#
#for k in range(1,nMr+1):
#    nMrF *= k

combinacion = nF/(rF*(nMrF))

print("La combinacion es:", int(combinacion))