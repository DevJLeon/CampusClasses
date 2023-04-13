print("\n Bienvenido a la calculadora de combinaciones.")

n = int(input("Ingrese la el total de objetos a combinar"))
r = int(input("Ingrese la el tamaño del grupo muestra"))
numerador = 1
rF = 1
nMrF = 1
nMr= n-r
for i in range(1, n+1):
    numerador *= i

for j in range(1, r+1):
    rF *= j

for k in range(1,nMr+1):
    nMrF *= k

combinacion = numerador/(rF*(nMrF))

print("La combinacion es:", int(combinacion))