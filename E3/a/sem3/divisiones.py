#diosito ayudame
#Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

#     Vamos a crear las siguientes funciones para trabajar con funciones:

##    Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
##    Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
##    Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
#     Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
##    Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe #     simplificar la fracción resultado.
##    Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
##    Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
#     Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
#
continuar = 1
fraccion1 = []
fraccion2 = []

def simpliFraccion(a,b):
    for i in range(5):
        if (a % 10  == 0 and b % 10 == 0):
            a /=10
            b /=10
        elif (a % 5 == 0 and b % 5 == 0):
            a /= 5
            b /= 5
        elif (a % 3 == 0 and b % 3 == 0):
            a /= 3
            b /= 3
        elif (a % 2 == 0 and b % 2 == 0):
            a /= 2
            b /= 2

def leerFraccion(orden):

    if orden == 1:
        numer = (int(input("Ingrese el numerador de la primera fraccion:\t")))
        denom = (int(input("Ingrese el denominador de la primera fraccion:\t")))
    elif orden == 2:
        numer = (int(input("Ingrese el numerador de la segunda fraccion:\t")))
        denom = (int(input("Ingrese el denominador de la segunda fraccion:\t")))

    for i in range(30):
        if (numer % 10  == 0 and denom % 10 == 0):
            numer /=10
            denom /=10
        elif (numer % 5 == 0 and denom % 5 == 0):
            numer /= 5
            denom /= 5
        elif (numer % 3 == 0 and denom % 3 == 0):
            numer /= 3
            denom /= 3
        elif (numer % 2 == 0 and denom % 2 == 0):
            numer /= 2
            denom /= 2
    return  [int(numer)],[int(denom)]

def escribirFraccion (a,b):
    if b == 1:
        return print(a)
    else:
        return print(a,"/",b)

def sumarFraccion (a1,b1,a2,b2):
    num = (a1*b2)+(b1*a2)
    den = (b1*b2)
    return print("\nLa suma de las fracciones es", str(a1)+"/"+str(b1), "+",str(a2)+"/"+str(b2), "=", str(num)+"/"+str(den), "=", num/den)

def restarFraccion (a1,b1,a2,b2):
    num = (a1*b2)-(b1*a2)
    den = (b1*b2)
    return print("\nLa resta de las fracciones es", str(a1)+"/"+str(b1), "-",str(a2)+"/"+str(b2), "=", str(num)+"/"+str(den), "=", num/den)

def multipFraccion (a1,b1,a2,b2):
    num = (a1*a2)
    den = (b1*b2)
    return print("\nLa multiplicacion de las fracciones es", str(a1)+"/"+str(b1), "*",str(a2)+"/"+str(b2), "=", str(num)+"/"+str(den), "=", num/den)

def diviFraccion(a1,b1,a2,b2):
    num = (a1*b2)
    den = (b1*a2)
    return print("\nLa division de las fracciones es", str(a1)+"/"+str(b1), "/",str(a2)+"/"+str(b2), "=", str(num)+"/"+str(den), "=", num/den)

def menu():
    opcion = int(input("\n\nIngrese la opcion de la operacion que desee realizar:\n1. Sumar dos fracciones\n2. Restar dos fracciones\n3. Multiplicar dos fracciones\n4. Dividir dos fracciones\n5. SALIR\n:::::::::::::::::::::::::::::::: "))

    if opcion == 1:
        fraccion1.append(leerFraccion(1))
        fraccion2.append(leerFraccion(2))
        sumarFraccion(fraccion1[0][0][0],fraccion1[0][1][0],fraccion2[0][0][0],fraccion2[0][1][0])
        menu()
    elif opcion == 2:
        fraccion1.append(leerFraccion(1))
        fraccion2.append(leerFraccion(2))
        restarFraccion(fraccion1[0][0][0],fraccion1[0][1][0],fraccion2[0][0][0],fraccion2[0][1][0])
        menu()
    elif opcion == 3:
        fraccion1.append(leerFraccion(1))
        fraccion2.append(leerFraccion(2))
        multipFraccion(fraccion1[0][0][0],fraccion1[0][1][0],fraccion2[0][0][0],fraccion2[0][1][0])
        menu()
    elif opcion == 4:
        fraccion1.append(leerFraccion(1))
        fraccion2.append(leerFraccion(2))
        diviFraccion(fraccion1[0][0][0],fraccion1[0][1][0],fraccion2[0][0][0],fraccion2[0][1][0])
        menu()
    elif opcion == 5:
        print("\nAdios popo")
#######################################################################################################################################################################################################################
menu()

#escribirFraccion(fraccion1[0][0][0],fraccion1[0][1][0])