import json

dict = {
    "EMPRESA": {
        "PERSONAS": [
            {"id": 1,
             "nombre": "Pedro",
             "edad": 20,
             "numDoc": 123456789
             },
            {"id": 2,
             "nombre": "Ofelia",
             "edad": 30,
             "numDoc": 123456788
             },
            {"id": 3,
             "nombre": "Ruth",
             "edad": 17,
             "numDoc": 123456799
             }
        ]
    }
}
try:
    with open("R3/sem5/empresa.json", "r") as archivo:
        None
except:
    with open("R3/sem5/empresa.json", "w") as archivo:
        json.dump(dict,archivo, indent=4)
# ********************************************************** FUNCIONES ************************************************************

def create(file = "R3/sem5/empresa.json"):
    nombre = input("Ingrese el nombre: \t")
    edad = int(input("Edad: \t"))
    doc = int(input("Numero de documento sin espacios ni comas EJ (10055444323): \t"))
    with open(file, "r+") as data:
        access_data = json.load(data)
        personas = access_data["EMPRESA"]["PERSONAS"]
        id = (len(personas)+1)
        datos ={
            "id":id,
            "Nombre":nombre,
            "Edad": edad,
            "numDoc":doc            
        }
        personas.append(datos)
        with open(file, "w") as data:
            json.dump(access_data,data, indent=4)
    for persona in personas:
        print (persona)

def read():
    None

def update():
    None
        
def delete():
    None

# ******************************************************** CODIGO *****************************************************************


optMenu = int(input("1.CREAR 2.LEER \n3.ACTUALIZAR 4.ELIMINAR\n"))
while optMenu != 0:
    if optMenu == 1:
        create()
    elif optMenu == 2:
        read()
    elif optMenu == 3:
        update()
    elif optMenu == 4:
        delete()
    optMenu = int(input("1.CREAR 2.LEER \n3.ACTUALIZAR 4.ELIMINAR\n"))


