import io
import json
#archivo = open("./a/sem3/diccionario.txt","w")
#archivo.write("Hola")
#archivo.close()
#nombre = "\nJuan Esteban Navas"
#archivo = open("./a/sem3/diccionario.txt", "a")#("w" sobreescribe, "a" adiciona)
#archivo.write(nombre)
#archivo.close()

#archivo = open("./a/sem3/diccionario.txt", "r")
#print(archivo.read())
#archivo.close()

#ARCHIVOS JSON

lista = ["Juan", "Esteban", "Camila"]
#archivo = open("./a/sem3/diccionario.json", "w")
diccionario = {"Nombre":"Pedro", "Apellido": "Cardozo", "cedula":"10044432345"}

#with open ("./a/sem3/diccionario.json", "w") as archivo:
#    json.dump(diccionario,archivo)

with open ("./a/sem3/diccionario.json", "r") as archivo:
    imprimir = json.load(archivo)

archivo.close()
print(imprimir)