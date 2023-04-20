import io

#archivo1= open("archivo01.txt","w+")
#primeraLinea = input("Ingrese lo que contendrá la primera línea: \t")
#seguir = int(input("¿Desea continuar? \n1.SI 0.NO \n"))
#siguienteLinea =primeraLinea+"\n"
#while seguir != 0:
#    adicion = input("Ingrese la siguiente linea: \n")
#    siguienteLinea += adicion + "\n"
#    seguir = int(input("¿Desea continuar? \n1.SI 0.NO \n"))
#archivo1.write(siguienteLinea)
#archivo1.close()


archivo1= open("archivo01.txt","r")
linea = archivo1.readlines()
leerLinea = int(input("¿Qué linea desea leer?: (presione 0 para salir) \t"))

while leerLinea != 0:
    if leerLinea < len(linea)+1:
        print("\n",linea[leerLinea-1])
        leerLinea = int(input("¿Qué linea desea leer?: (presione 0 para salir) \t"))   
    else:   
        print("La linea no existe. El texto tiene", len(linea), "lineas. Por favor inténtelo de nuevo\n")
        leerLinea = int(input("¿Qué linea desea leer?: (presione 0 para salir) \t"))

