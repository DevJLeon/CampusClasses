#1. CREAR 2. APERTURA 3. MANIPULACION 4. CIERRE
#   OPEN     WRITE       READ /READLINES  CLOSE
import io
archivo = open("R3/sem5/nombres.txt","w")

nom = "Sergio Medina \nLuisa Ruiz \nMario Moreno"
archivo.write(nom)

archivo.close()