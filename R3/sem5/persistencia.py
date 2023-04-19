#1. CREAR 2. APERTURA 3. MANIPULACION 4. CIERRE
#   OPEN     WRITE       READ /READLINES  CLOSE
import io
archivo = open("R3/sem5/nombres.txt","r")

#nom = "Sergio Medina \nLuisa Ruiz \nMario Moreno"
#archivo.write(nom)
lista = archivo.readlines()
archivo.close()
print(lista)

for i in range(len(lista)):
    print("nombre:", lista[i])