##salu2
contadores = [[0],[0],[0],[0]]
continuar = True

########################################################################
def ventaBoletas (cantidad, tipo):
    if tipo == 1:
        total = cantidad * 50
    elif tipo == 2:
        total = cantidad * 75
    elif tipo == 3:
        total = cantidad * 100
    return str(total) + "$USD"
########################################################################

while continuar == True:
    tipo = int(input("Ingrese el tipo de boleta (1. GENERAL  2. VIP  3. PLATINUM): "))
    cantidad = int(input("Ingrese la cantidad de boletas: "))
    if tipo == 1:
        contadores[0].append(cantidad)
        contadores[3].append(cantidad * 50)
    elif tipo == 2:
        contadores[1].append(cantidad)
        contadores[3].append(cantidad * 75)
    elif tipo == 3:
        contadores[2].append(cantidad)
        contadores[3].append(cantidad * 100)
    print(ventaBoletas(cantidad, tipo))
    continuar=int(input("¿Desea continuar? (0.No   1.Si)"))

print("La cantidad de boletas vendidas fue: \n General:     ", sum(contadores[0]), "\n VIP    : ", sum(contadores[1]), "\n PLATINUM:     ", sum(contadores[2]), "\n Total de ventas: ", sum(contadores[3]), "$USD")