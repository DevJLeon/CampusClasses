import json 

#se abre con open 
#almacenar en el archivo json: dump
#leer archivo: load

lista = [1,2,3,4,5,10,30,40,55]
dict = {"1":"uno","2":"dos","3":"tres","4":"cuatro"}

with open("R3/sem5/lista.json") as archivo:
    leerArchivo = json.load(dict,archivo)


print(leerArchivo["3"])