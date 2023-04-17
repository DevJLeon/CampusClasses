#Se realiza la compra de N articulos donde se ingresa el código del artículo y la cantidad. Y mediante el uso de diccionarios para los nombres y valores unitarios de los artículos, el programa debe obtener el nombre de cada artículo, cantidad comprada, valor unitario, valor total y la cantidad comprada. Finalmente calcular el valor total de la compra.


articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}

valores = {1:2500,2:3800,3:1200,4:35000,5:3700}

n = int(input("Ingrese la cantidad de artículos(TOTAL)\t"))

total = 0
for i  in range(n):
    print(articulos)
    articulo = int(input("Ingrese el ("+ str(i+1) +") articulo:\t"))
    print("valor unitario de", articulos[articulo], "es:\t",valores[articulo])
    cantidad = int(input("Ingrese la cantidad de "+ str(articulos[articulo])+ " a comprar:\t"))
    total += valores[articulo]*cantidad
    
print("El total es: $", total)