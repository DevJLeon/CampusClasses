#Se realiza la compra de N articulos donde se ingresa el código del artículo y la cantidad. Y mediante el uso de diccionarios para los nombres y valores unitarios de los artículos, el programa debe obtener el nombre de cada artículo, cantidad comprada, valor unitario, valor total y la cantidad comprada. Finalmente calcular el valor total de la compra.
def contadorVenta(idArticulo,cantidad):
    factura.append({"id":idArticulo,"nombre":articulos[idArticulo],"precioUnitario":valores[idArticulo],"cantidad":cantidad, "total":(valores[idArticulo]*cantidad)},)
    return factura

articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores = {1:2500,2:3800,3:1200,4:35000,5:3700}
factura = []
mostrarFactura = "ID \t \t ARTICULO \t \t PRECIO UNIDAD \t \t CANTIDAD \t \t TOTAL \n"
total = 0


n = int(input("Ingrese la cantidad de artículos(TOTAL)\t"))

for element in articulos:
        print(element,articulos[element])
        
for i  in range(n):
    articulo = int(input("Ingrese el ("+ str(i+1) +") articulo:\t"))
    print("valor unitario de", articulos[articulo], "es:\t",valores[articulo])
    cantidad = int(input("Ingrese la cantidad de "+ str(articulos[articulo])+ " a comprar:\t"))
    total += valores[articulo]*cantidad
    
    contadorVenta(articulo,cantidad)
    
print("El total es: $", total)

for item in factura:
    mostrarFactura+= str(str(item["id"])+ " \t \t" +str(item["nombre"])+ " \t \t \t" +str(item["precioUnitario"])+ " \t \t \t" +str(item["cantidad"])+ " \t \t \t" +str(item["total"])+"\n")
    
print(mostrarFactura)