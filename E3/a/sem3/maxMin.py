## Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
## Made by JLeonDev
canNum = int(input("Ingrese la cantidad de nùmeros a ingresar :)\t"))
numeros = []

for i in range(canNum):
        numeros.append(int(input("Ingrese el nùmero")))

def calcularMinMax(arreglo):
    nuMayor = 0
    nuMenor = arreglo[0]
    for i in arreglo:
        if i > nuMayor:
            nuMayor = i
        elif i < nuMenor:
             nuMenor = i
    return print("El numero mayor es",  nuMayor, "y el nùmero menor es", nuMenor)

calcularMinMax(numeros)