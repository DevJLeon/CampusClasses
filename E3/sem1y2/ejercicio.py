## la institucion educativa sameduca cuenta con N docentes, conociendo de cada uno de ellos su nùmero de cèdula,
## nombre y categorìa y nùmero de horas laboradas en el mes. Se pide realizar un programa que calcule el valor de los honorarios
## de cada docente y el valor total a pagar por concepto de honorarios. Para este proceso, nos suministran el diccionario
## donde se define el valor de la hora para cada categorìa:

diccionario_categoria={1:25000,2:30000,3:40000,4:45000,5:60000}

cantProfe = int(input("Ingrese la cantidad de docentes:\t"))
profesores = {}
totalHonorarios = 0

for i in range(cantProfe):
    valHonorarios=0
    profesores["p"+str(i)] ={
        "nombre":input("Ingrese el nombre del profesor:\t"),
        "cedula":int(input("Ingrese la cedula del profesor(sin puntos ni espacios):\t")),
        "categoria":int(input("Ingrese la categoria:\t")),
        "numHoras":int(input("Ingrese la cantidad de horas laboradas:\t")),
        "valor Honorarios":()
    }
    if profesores["p"+str(i)]["categoria"]== 1:
        valHonorarios = profesores["p"+str(i)]["numHoras"]*diccionario_categoria[1]
    elif profesores["p"+str(i)]["categoria"]== 2:
        valHonorarios = profesores["p"+str(i)]["numHoras"]*diccionario_categoria[2]
    elif profesores["p"+str(i)]["categoria"]== 3:
        valHonorarios = profesores["p"+str(i)]["numHoras"]*diccionario_categoria[3]
    elif profesores["p"+str(i)]["categoria"]== 4:
        valHonorarios = profesores["p"+str(i)]["numHoras"]*diccionario_categoria[4]
    elif profesores["p"+str(i)]["categoria"]== 5:
        valHonorarios = profesores["p"+str(i)]["numHoras"]*diccionario_categoria[5]
    profesores["p"+str(i)]["valor Honorarios"]= valHonorarios
    totalHonorarios += valHonorarios
    print("Los honorarios del docente", profesores["p"+str(i)]["nombre"], "son $"+(str(profesores["p"+str(i)]["valor Honorarios"])))

print("El valor total de los honorarios es: $" + str(totalHonorarios))