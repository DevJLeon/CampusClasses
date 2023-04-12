##  
## 
## 

## def nombreCompleto(nombre,apellido):
##     print(nombre,apellido)
## 
## def obtenerNombreCompleto(nombre,apellido):
##     return nombre + " " + apellido
## 
## print(obtenerNombreCompleto("Juan", "Gonzales"))
## 
## nombreCompleto("Juan", "Gonzales")
## 

'''
para un concierto hay 3 tipos de boletas
desarrollar un programa que calcule el total de ventas para cada boleta
(cuantas boletas se vendieron de cada tipo y cuanto se recaudò por boleta)
en cada venta se pueedn vender mas de una boleta pero solo del mismo tipo

    ubicacion    valor
1   general       50
2   vip           75
3   platinum      100  
'''
contGene = 0
contVIP = 0
contPlat = 0
contTotal = contGene+contVIP+contPlat
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
        contGene += cantidad
        contTotal += cantidad * 50
    elif tipo == 2:
        contVIP += cantidad
        contTotal += cantidad * 75
    elif tipo == 3:
        contPlat += cantidad
        contTotal += cantidad * 100
    print(ventaBoletas(cantidad, tipo))
    continuar=int(input("¿Desea continuar? (0.No   1.Si)"))

print("La cantidad de boletas vendidas fue: \n General:     ", contGene, "\n VIP    : ", contVIP, "\n PLATINUM:     ", contPlat, "\n Total de ventas: ", contTotal, "$USD")