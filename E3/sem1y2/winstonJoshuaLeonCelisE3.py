## 1.   Crea una aplicación que nos calcule el área de un círculo, cuadrado o triangulo.
## Pediremos qué figura queremos calcular, su área y según lo introducido pedirá los valores
## necesarios para calcular el área. Crea una función por cada figura para calcular cada área,
## este devolverá un número real. Muestra el resultado por pantalla
##     Circulo: (radio^2)*PI
##     Triangulo: (base * altura) / 2
##     Cuadrado: lado * lado
##
## 2.  Crea una aplicación que nos pida un número por teclado y con una función se lo pasamos
## por parámetro para que nos indique si es o no un número primo, debe devolver true si
## es primo sino false.
## Un número primo es aquel solo puede dividirse entre 1 y si mismo.
## Por ejemplo: 25 no es primo, ya que 25 es divisible entre 5, sin embargo, 17 si es primo.
##    
## 3.  Crea una aplicación que nos calcule el factorial de un número pedido por teclado, lo
## realizara mediante una función al que le pasamos el número como parámetro. Para calcular el
## multiplica los números anteriores hasta llegar a uno. Por ejemplo, si introducimos un 5,
## realizara esta operación 5*4*3*2*1=120.
## 
## 4.  Crea una aplicación que nos convierta una cantidad de pesos introducida por teclado a otra
## moneda, estas pueden ser a dolares, yenes o libras. La función tendrá como parámetros, la
## cantidad de pesos y la moneda a pasar que será un texto
## 
## 5. Crea una aplicación que replique la ecuación cuadrática, solicitando los valores para
## a, b y c. Tener en cuenta que se debe validar si los valores dados por el usuario generan un
## resultado imaginario, de ser así debe informarse
## 
continuar = True

## ********************************************************FUNCIONES************************************************************
def menu():
    proceso = int(input("¿Què proceso desea realizar? \n1.areas 2. primos. 3. Factorial 4. PesoConverter 5. ResolverCuadràtica:\t"))
    if proceso == 1:
        calcularArea()
    elif proceso == 2:
        primo()
    elif proceso == 3:
        factorial()
    elif proceso == 4:
        valor = float(input("Ingrese la cantidad de pesos(COP)"))
        moneda = input("Ingrese la moneda a convertir:\n\t DOLAR // YEN // LIBRA(libra esterlina): ")
        pesoConverter(valor,moneda)
    elif proceso == 5:
        print("RECUERDE: (Formula general) ax**2 +- bx + c")
        a=int(input("Ingrese el valor de a:\t"))
        b=int(input("Ingrese el valor de b:\t"))
        c=int(input("Ingrese el valor de c:\t"))
        cuadraticaSolver(a,b,c)

def calcularArea():
    figure = input("Bienvenido a la calculadora de àreas. Por favor indique la figura a hallar àrea. \n\tCIRCULO // TRIANGULO // CUADRADO\n")
    if figure.upper() == "CIRCULO":
        radius = float(input("Indique el radio del circulo: "))
        return print("El area de su circulo es",(radius**2)*3.1416)
    elif figure.upper() == "TRIANGULO":
        base = float(input("Indique la base del triangulo: "))
        height = float(input("Indique la altura del triangulo: "))
        return print("El area de su triangulo es",(base*height)/2)
    elif figure.upper() == "CUADRADO":
        side = float(input("Indique la medida de uno de los lados de la figura: "))
        return print("El area de su cuadrado es",side*side)

def primo():
    numero = int(input("Introduce un número: "))
    for i in range(2,numero):
        if numero % i == 0:
            return print("El número",numero,"es primo")
    return print("El número",numero,"no es primo")

def factorial():
    numero = int(input("Introduce un número: "))
    resultadoFactorial = numero
    for i in range(1,numero):
        None
        resultadoFactorial = (resultadoFactorial*i)
    return print("El factorial es:",resultadoFactorial)

def pesoConverter(pesos,moneda):
    if moneda.upper() == "DOLAR":
        final = pesos / 4743.94
        return print("La conversion es:", pesos, "$COP equivale a", final,"$USD")
    elif moneda.upper() == "YEN":
        final = pesos / 36.27
        return print("La conversion es:", pesos, "$COP equivale a", final,"¥YEN")
    elif moneda.upper() == "LIBRA":
        final = pesos / 5828.55
        return print("La conversion es:", pesos, "$COP equivale a", final,"£LIBRA")
    
def cuadraticaSolver(a,b,c):
    ##comprobar si esta monda es imaginaria o no
    if ((b**2)-(4*a*c))< 0:
        print("X es imaginario :)")

    x1 = ((-1*b)+(((b**2)-(4*a*c))**(1/2)))/(2*a)
    x2 = ((-1*b)-(((b**2)-(4*a*c))**(1/2)))/(2*a)
    return print("X_1 =",x1,"X_2=", x2)

    
## ********************************************************/FUNCIONES************************************************************

while continuar == True:
    menu()
    continuar = int(input("¿Desea continuar?\t1. Si\t 2. No:\t"))