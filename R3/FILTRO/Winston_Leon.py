import json
import time

ruta = "R3/FILTRO/AutoShopping.json"

with open (ruta, "r") as data:
    access_data = json.load(data)
    store = access_data["autostore"]
    autos = store["auto"]
    
#*********************************************************************************************** FUNCTIONS **************************************************************************
    
def save():
    with open(ruta, "w") as data:
        json.dump(access_data, data, indent=4)

def crearAuto ():
    marca = input("Ingrese la marca del vehículo: \t")
    linea = input("Linea del vehículo: \t")
    modelo = int(input("Modelo: \t"))
    precio = int(input("Precio: \t"))
    equipamiento = input("Ingrese el Equipamiento del vehículo: \t")
    optEquip = int(input("¿Desea añadir algo más al equipamiento del vehículo?: \t 1.SI 2.NO \t"))
    if optEquip == 1:
        listaEquipamiento = []
        listaEquipamiento.append(equipamiento)
        while optEquip == 1:
            equipamiento = input("Ingrese el Equipamiento del vehículo: \t")
            listaEquipamiento.append(equipamiento)
            optEquip = int(input("¿Desea añadir algo más al equipamiento del vehículo?: \t 1.SI 2.NO \t"))
    else:
        listaEquipamiento = equipamiento
        
    newAuto = {"marca":marca,
               "linea":linea,
               "modelo":modelo,
               "precio":precio,
               "equipamiento":listaEquipamiento,
               }
    autos.append(newAuto)
    save()
    
def showCars ():
    for auto in autos:
        print("\n------------------------------------------------------------\nMarca:",
              auto["marca"]+"\nlinea:",auto["linea"],
              "\nModelo:", auto["modelo"],
              "\nPrecio:",auto["precio"],
              "\nEquipamiento:"
              )
        if type(auto["equipamiento"]) == list:
            for equip in auto["equipamiento"]:
                print("*", equip)
        else:
            print("*", auto["equipamiento"])
        time.sleep(0.5)

def showByBrand ():
    marcas = []
    idMarca = 0
    for auto in autos:
        if auto["marca"] in marcas:
            continue
        else:
            marcas.append(auto["marca"])
    for marca in marcas:
        print(str(idMarca+1)+".",marca, end="     /     ")
        idMarca+=1
    idMarca=(int(input("\nSeleccione una marca:(ID) ")))
    
    for auto in autos:
        if auto["marca"]== marcas[idMarca-1]:
            print("\n-------------------------------------------------\nLinea:",auto["linea"],"\nModelo:", auto["modelo"],"\nPrecio:",auto["precio"],"\nEquipamiento:")
            
            if type(auto["equipamiento"]) == list:
                for equip in auto["equipamiento"]:
                    print("*", equip)
            else:
                print("*", auto["equipamiento"])
            time.sleep(0.5)

def updateCar ():
    id = 0
    for auto in autos:
        print("\n------------------------------------------------------------\nID DEL VEHÍCULO:",id,"\nMarca:",
              auto["marca"]+"\nlinea:",auto["linea"],
              "\nModelo:", auto["modelo"],
              "\nPrecio:",auto["precio"],
              "\nEquipamiento:"
              )
        if type(auto["equipamiento"]) == list:
            for equip in auto["equipamiento"]:
                print("*", equip)
        else:
            print("*", auto["equipamiento"])
        id +=1
        time.sleep(0.5)
        
    updateID = int(input("Indique el ID del carro que desea actualizar: \t"))
    autoMod = autos[updateID]
    
    changes = int(input("¿Qué desea modificar?\n 1. Marca \t 2.linea \n3.modelo \t 4.precio \n5.equipamiento \t 0.NADA(salir)\n"))
    while changes != 0:
        if changes == 1:
            autoMod["marca"] = input("Ingrese la nueva marca: \t")
        elif changes == 2:
            autoMod["linea"] = input("Ingrese la nueva linea: \t")
        elif changes == 3:
            autoMod["modelo"] = int(input("Ingrese el nuevo modelo: \t"))
        elif changes == 4:
            autoMod["precio"] = int(input("Ingrese el nuevo precio: \t"))
        elif changes == 5:
            equipamiento = input("Ingrese el nuevo Equipamiento del vehículo: \t")
            optEquip = int(input("¿Desea añadir algo más al equipamiento del vehículo?: \t 1.SI 2.NO \t"))
            if optEquip == 1:
                listaEquipamiento = []
                listaEquipamiento.append(equipamiento)
                while optEquip == 1:
                    equipamiento = input("Ingrese el Equipamiento del vehículo: \t")
                    listaEquipamiento.append(equipamiento)
                    optEquip = int(input("¿Desea añadir algo más al equipamiento del vehículo?: \t 1.SI 2.NO \t"))
            else:
                listaEquipamiento = equipamiento
            autoMod["equipamiento"] = listaEquipamiento
        changes = int(input("¿Qué desea seguir modificando en este vehículo?\n 1. Marca \t 2.linea \n3.modelo \t 4.precio \n5.equipamiento \t 0.NADA(salir)\n"))
    save()
    
def deleteCar ():
    id = 0
    for auto in autos:
        print("\n------------------------------------------------------------\nID DEL VEHÍCULO:",id,"\nMarca:",
              auto["marca"]+"\nlinea:",auto["linea"],
              "\nModelo:", auto["modelo"],
              "\nPrecio:",auto["precio"],
              "\nEquipamiento:"
              )
        if type(auto["equipamiento"]) == list:
            for equip in auto["equipamiento"]:
                print("*", equip)
        else:
            print("*", auto["equipamiento"])
        id +=1
        time.sleep(0.5)
        
    deleteID = int(input("Indique el ID del carro que desea eliminar de la lista: \t"))
    
    autos.pop(deleteID)
    save()


#************************************************************************************************* BODY *****************************************************************************

optMenu = int(input("\n\n¿Qué desea hacer \n 1.Añadir auto \t \t 2.Ver autos \n 3.Actualizar auto \t 4.Eliminar auto \n 0. SALIR: \n"))

while optMenu > 0:
    if optMenu == 1:
        crearAuto()
    elif optMenu == 2:
        optShowCar = int(input("¿Qué desea hacer? 1. Ver todos los carros \t 2.Ver por marca \n"))
        if optShowCar == 1:
            showCars()
        elif optShowCar == 2:
            showByBrand()
    elif optMenu == 3:
        updateCar()
    elif optMenu == 4:
        deleteCar()
    optMenu = int(input("\n\n¿Qué desea hacer \n 1.Añadir auto \t \t 2.Ver autos \n 3.Actualizar auto \t 4.Eliminar auto \n 0. SALIR: \n"))