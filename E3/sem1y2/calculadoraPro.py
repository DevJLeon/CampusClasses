##No se detiene hasta que lo indique, contador de operaciones, resultado

n1 = int(input("Indique el primer número: "))

operacion = input("\nIndique que operación se realizará: S (suma), R (resta), M(multiplicación, D(división), P (potenciación): )").upper()

n2 = int(input("Indique el segundo número: "))

acumulado = 0


##******************************contadores**************************************
contSuma = 0
contResta = 0
contMulti = 0
contDivi = 0
contPote = 0
##******************************************************************************

##******************************Funciones***************************************
def operar(acumulado, operacion, siguienteNumero):
    if operacion == "S":
        acumulado += siguienteNumero
    elif operacion == "R":
        acumulado -= siguienteNumero
    elif operacion == "M":
        acumulado *= siguienteNumero
    elif operacion == "D":
        acumulado /= siguienteNumero
    elif operacion == "P":
        acumulado = acumulado ** siguienteNumero
    return acumulado


def SiguienteNumero():
    return(int(input("Ingrese el siguiente número")))
##******************************************************************************

print(operar(n1, operacion, n2))

continuar = input("¿Desea continuar? S/N: ").upper()

while continuar == "S":
    operacion = input("\nIndique que operación se realizará: S (suma), R (resta), M(multiplicación, D(división), P (potenciación): )").upper()
    print(operar(acumulado, operacion, SiguienteNumero()))

    continuar = input("¿Desea continuar? S/N").upper()
    if continuar == "N":
        break


##********************Cantidad Total de operaciones********************

print("\ncantidad de Sumas =", contSuma, "\ncantidad de restas=", contResta, "\nCantidad de multiplicaciones =", contMulti, "\nCantidad de diviciones =", contDivi, "\ncantidad de potenciaciones =", contPote)