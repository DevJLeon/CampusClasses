import time
optMenu = 1
#############################################         DICCIONARIOS       ##################################################################################################

dicEstudiantes = {
    1:{
    "nombres":"Juan Gavioto",
    "apellidos":"Gonzales Mora",
    "correo":"jgavmora@gmail.com"
    },
    2:{
    "nombres":"Daniela",
    "apellidos":"Estupinhan Garcia",
    "correo":"jgavmora@gmail.com"
    },
    3:{
    "nombres":"Santiago",
    "apellidos":"Lopez Aguilar",
    "correo":"jgavmora@gmail.com"
    },
    4:{
    "nombres":"Jonathan",
    "apellidos":"Maldonado Gutierrez",
    "correo":"jgavmora@gmail.com"
    },
    5:{
    "nombres":"Milthon",
    "apellidos":"Lopez Obrador",
    "correo":"jgavmora@gmail.com"
    },
    6:{
    "nombres":"Santiago",
    "apellidos":"Peña Nieto",
    "correo":"jgavmora@gmail.com"
    },
}

dicMaterias = {
    1:{"nomMateria":"Matematicas"},
    2:{"nomMateria":"Biologia"},
    3:{"nomMateria":"Fisica"},
    4:{"nomMateria":"Quimica"}
}

dicNotas ={
    1:{"idEstudiante":"",
       "idMateria":"",
       "nota1":"",
       "nota2":"",
       "nota3":"",
       "notaFinal":""
       }
}

###########################################          FUNCIONES NOTAS          ######################################################################################

def agregarNotas(diccionario, idEstudiante, idMateria, nota1, nota2, nota3):
    id = crearId(diccionario)

    diccionario[id+1] = {
        "idEstudiante":idEstudiante,
        "idMateria":idMateria,
        "nota1":nota1,
        "nota2":nota2,
        "nota3":nota3,
        "notaFinal":((nota1+nota2+nota3)/3),
        }
    return diccionario

def verNotas(diccionario,id):
    listaNotas = ""
    nombre = str(dicEstudiantes[id]["nombres"])+" \t"+str(dicEstudiantes[id]["apellidos"])
    materia = str(dicMaterias[(dicNotas[id]["idMateria"])]["nomMateria"])
    for nota in diccionario:
        listaNotas += (str(nota) + "\t" + nombre + " \t\t" + materia+ "\n")
    return print(listaNotas)

def editarNotas(diccionario, id, key,cambio):
    diccionario[id][key] = cambio


#############################################       FUNCIONES MATERIAS    ##################################################################################################

def crearId(diccionario):
    id = list(diccionario.keys())[len(diccionario)-1]
    return id

def agregarMateria(materia, nombreMateria):
    id = crearId(materia)
    materia[id+1] = {"nomMateria":nombreMateria}
    return materia

def verMaterias(materias):
    listaMaterias = ""
    for materia in materias:
        listaMaterias += str(materia) + " " + str(materias[materia]["nomMateria"]+"\n")
    return listaMaterias

def editarMateria(diccionario, id, newName):
    diccionario[id] = {"nomMateria": newName}

###########################################          FUNCIONES ESTUDIANTES          ######################################################################################

def agregarEstudiante(diccionario, nombreEstudiante, apellidoEstudiante, correo):
    id = crearId(diccionario)

    diccionario[id+1] = {
        "nombres":nombreEstudiante,
        "apellidos":apellidoEstudiante,
        "correo":correo
        }
    return diccionario

def verEstudiantes(diccionario):
    listaEstudiantes = ""
    for estudiante in diccionario:
        listaEstudiantes += (str(estudiante) + "\t" + str(diccionario[estudiante]["nombres"]) + " \t" + str(diccionario[estudiante]["apellidos"]) + " \t\t" + str(diccionario[estudiante]["correo"]) + "\n")
    return print(listaEstudiantes)

def editarEstudiante(diccionario, id, key,cambio):
    diccionario[id][key] = cambio

def delete(diccionario):
        codigo = int(input("Ingrese el codigo de la ID a elminiar: \t"))
        del(diccionario[codigo])
#############################################            MENUS            ##################################################################################################

def menuMaterias(materias):
    print("*********************************************MATERIAS**************************************************************")
    opcion = int(input("\n\nSeleccione alguna de las siguientes opciones:\n1.Agregar \t 2.Editar\n3.Eliminar \t 0.Volver\n"))

    if opcion == 1:
        nomMateria = input("Ingrese el nombre de la materia: \t")
        agregarMateria(materias,nomMateria)
    elif opcion == 2:
        editarMateria(materias,int(input("Ingrese el ID de la materia a editar: \t")),input("Indique el nuevo nombre de la materia"))
        print("\n***MATERIA EDITADA CON ÈXITO***")
    elif opcion == 3:
        codigo = int(input("Ingrese el codigo de la materia a elminiar: \t"))
        del(dicMaterias[codigo])
    elif opcion == 0:
        print(verMaterias(dicMaterias))

def menuEstudiantes(diccionario):
    continueEdit = 1
    print("*********************************************MATERIAS**************************************************************")
    opcion = int(input("\n\nSeleccione alguna de las siguientes opciones:\n1.Agregar \t 2.Editar\n3.Eliminar \t 0.Volver\n"))

    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: \t")
        apellido = input("Ingrese el apellido del estudiante: \t")
        correo = input("Ingrese el correo del estudiante: \t")
        agregarEstudiante(diccionario,nombre,apellido,correo)
        print("****************************ESTUDIANTE AGREGADO CON EXITO********************************")
        time.sleep(2)
        verEstudiantes(diccionario)
    elif opcion == 2:
        while continueEdit == True:
            cambio = ""
            verEstudiantes(diccionario)
            IDestudiante = int(input("Indique el ID del estudiante a editar: \t"))
            key = int(input("Indique que desea editar del estudiante: \n1.Nombres \t2.Apellidos \n3.Correo: \t"))
            if key == 1:
                key = "nombres"
                cambio = input("Inserte nombre(s) modificado: \t")
            elif key == 2:
                key = "apellidos"
                cambio = input("Inserte apellido(s) modificado: \t")
            elif key == 3:
                key = "correo"
                cambio = input("Inserte correo(s) modificado: \t")
            editarEstudiante(diccionario,IDestudiante,key,cambio)
            continueEdit = int(input("?Desea continuar?"))
    elif opcion == 3:
        verEstudiantes(diccionario)
        delete(diccionario)
    elif opcion == 0:
        verEstudiantes(diccionario)

def menuNotas(diccionario):
    continueEdit = 1
    print("*********************************************NOTAS**************************************************************")
    opcion = int(input("\n\nSeleccione alguna de las siguientes opciones:\n1.Agregar \t 2.Editar\n3.Eliminar \t 0.Volver\n"))

    if opcion == 1:
        idAlumno = int(input("Ingrese el ID del alumno: "))
        idMateria = int(input("Ingrese el ID de la materia: "))
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))
        agregarNotas(diccionario,idAlumno,idMateria,nota1,nota2,nota3)
        print("****************************NOTA AGREGADA CON EXITO********************************")
        verNotas(diccionario,)
    elif opcion == 2:
            None
    elif opcion == 3:
        delete(diccionario)
    elif opcion == 0:
        None

#############################################          ACCIONES           ##################################################################################################

while optMenu != 0:
    optMenu = int(input("\n\nSeleccione alguna de las siguientes opciones:\n1.Notas \t 2.Estudiantes\n3.Materias \t 0.Salir\n"))
    if optMenu == 1:
        menuNotas(dicNotas)
    elif optMenu == 2:
        menuEstudiantes(dicEstudiantes)
    elif optMenu == 3:
        menuMaterias(dicMaterias)
    else :
        print("Adios, cv")    

#print(verEstudiantes(dicEstudiantes))
#agregarMateria(dicMaterias,"Artes")
#print(dicMaterias)
##print(verMaterias(dicMaterias))