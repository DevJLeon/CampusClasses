##lista 5 profudctos or total venta

print("\n\n\n")

opcion = int(input("¿Desea crear una lista de compras o calcular el total de ventas? \n 1.Compras \n 2.Ventas\n"))

indice = 0
otro = "S"
lista = ""

cantidadLista = 0



if opcion == 1:
    lista = input("Ingrese un elemento a la lista: ")
    costo = float(input("Ingrese el costo del producto: \n"))
    cantidadLista += 1
    otro = input("¿Desea agregar otro elemento? S/N \n").upper()

    if otro == "S":
        while cantidadLista < 5:
            lista += ", " + input("\nIngrese un elemento a la lista: ")
            costo += float(input("\nIngrese un costo del elemento: "))
            cantidadLista += 1
            if cantidadLista == 5:
                break
            otro = input("\n¿Desea agregar otro elemento? S/N \n").upper()

    print("\nSu lista es: \n>> " + lista, "Y su subtotal es: \n", costo)
elif opcion == 2:
    precio = float(input("Ingrese el precio del producto"))
    otro = input("¿Desea agregar otro elemento? S/N \n").upper()
    while otro == "S":
        precio += float(input("\nIngrese un precio del elemento: "))
        otro = input("\n¿Desea agregar otro elemento? S/N \n").upper()
    print("\nEl precio total de los productos es :", precio)



    
