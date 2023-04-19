#////////////////////////////////////////////////////////////      EJERCICIO 1        ////////////////////////////////////////////////////////////////////////////////////////////////////////
import io



#////////////////////////////////////////////////////////////      EJERCICIO 2        ////////////////////////////////////////////////////////////////////////////////////////////////////////

def crearDirectorio ():
    archivo02=open("directorio.txt", "x")
    archivo02.close()
    
def consultarDirectorio ():
    archivo02 = open("directorio.txt", "r")
    for i in range(len(archivo02)):
        print(archivo02[i])
    archivo02.close()

def añadirCliente ():
    archivo02 = open("directorio.txt", "a")
    cliente = input("Ingrese el nombre del Cliente: \t")
    numero = int(input("Ingrese el numero del Cliente: \t"))
    dato = cliente + "," + numero +"\n"
    archivo02.write(dato)
    archivo02.close()

def eliminarCliente():
    archivo02 = open("directorio.txt", "w")

opt02 = int(input("1. Crear directorio \t 2. Consultar directorio \n3. Añadir nuevo cliente \t 4. Eliminar telefono \n 0. SALIR: \t"))
while opt02 != 0:
    if opt02 == 1:
        try:
            crearDirectorio()
        except:
            print("El directorio ya existe.")
    elif opt02 == 2:
        try:
            consultarDirectorio()
        except:
            print("El directorio no existe. Por favor créelo")
    elif opt02 == 3:
        try:
            añadirCliente()
        except:
            print("El directorio no existe. Por favor créelo")   
    elif opt02 == 4:
        None
        
    opt02 = int(input("1. Crear directorio \t 2. Consultar directorio \n3. Añadir nuevo cliente \t 4. Eliminar telefono \n 0. SALIR: \t"))


#////////////////////////////////////////////////////////////      EJERCICIO 3        ////////////////////////////////////////////////////////////////////////////////////////////////////////