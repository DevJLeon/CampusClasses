# 1. Crear grupos Básicos, Intermedio y avanzados con campers y sus datos personales (Nombre, Mes de Ingreso, Grupo y Edad.
#1.1 Registrar Expert Trainer Del grupo Básico.
#1.2 Buscar Campers duplicados en 2 grupos.
#1.3 Eliminar campers por inasistencia.
#1.4 Listar los Campers del grupo
#1.5 Traslado del camper de grupo (ej.: de intermedio a básico).
#1.6 Agregar Campers después del registro inicial, al grupo del expert trainer determinado.
#1.7 Reportar los campers de mayor y menor edad de cada grupo

CAMPUS = []


print("\n----------------------------------------------\n-----MANTENIMIENTO Y PREMIOS CAMPERS CAMPUS-----")

#********************************************************************  FUNCIONES **********************************************************************

def menu():
    print("----------------------------------------------")
    opcion = int(input("¿A qué grupo desea Acceder? \n1. Basico\n3. Intermedio\n3. Avanzado\n"))

    if opcion == 1:
        menuBasico()
    elif opcion == 2:
        menuIntermedio()
    elif opcion == 3:
        menuAvanzado()



def menuBasico():
    print("----------------------------------------------")
    opcion = float(input("0. TERMINAR PROCESO\n----------------------------------------------\n1. CREAR GRUPO BÁSICO CON CAMPERS Y SUS DATOS PERSONALES\n1.1. REGISTRAR EXPERT TRAINER DEL GRUPO BÁSICO\n1.2. BÚSQUEDA DE CAMPERS DUPLICADOS\n1.3. ELIMINACION DE CAMPERS POR INASISTENCIA\n1.4. LISTAR CAMPERS\n1.5. TRANSLADO DE CAMPER ENTRE GRUPOS POR NIVELACION\n1.6. AGREGAR CAMPERS AL GRUPO (despues del registro inicial)\n1.7. REPORTAR CAMPERS DE MAYOR Y MENOR EDAD\n"))
    while opcion != 0:
        if opcion == 1.0:
            createGroup(1)
            menuBasico()
        elif opcion == 1.1:
            try:
                addTrainer(CAMPUS[0])
                menuBasico()
            except:
                print("No existe la categoría aún. Por favor créela.")
        elif opcion == 1.2:
            None
        elif opcion == 1.3:
            None
        elif opcion == 1.4:
            None
        elif opcion == 1.5:
            None
        elif opcion == 1.6:
            None
        elif opcion == 1.7:
            None

def menuIntermedio():
    print("----------------------------------------------")
    opcion = float(input("0. TERMINAR PROCESO\n----------------------------------------------\n2. CREAR GRUPO AVANZADO CON CAMPERS Y SUS DATOS PERSONALES\n2.1. REGISTRAR EXPERT TRAINER DEL GRUPO AVANZADO\n2.2. BÚSQUEDA DE CAMPERS DUPLICADOS\n2.3. ELIMINACION DE CAMPERS POR INASISTENCIA\n2.4. LISTAR CAMPERS\n2.5. TRANSLADO DE CAMPER ENTRE GRUPOS POR NIVELACION\n2.6. AGREGAR CAMPERS AL GRUPO (despues del registro inicial)\n2.7. REPORTAR CAMPERS DE MAYOR Y MENOR EDAD\n"))

    if opcion == 2.0:
        createGroup(2)
    elif opcion == 2.1:
        print("2.1")
    elif opcion == 2.2:
        None
    elif opcion == 2.3:
        None
    elif opcion == 2.4:
        None
    elif opcion == 2.5:
        None
    elif opcion == 2.6:
        None
    elif opcion == 2.7:
        None

def menuAvanzado():
    print("----------------------------------------------")
    opcion = float(input("0. TERMINAR PROCESO\n----------------------------------------------\n3. CREAR GRUPO INTERMEDIO CON CAMPERS Y SUS DATOS PERSONALES\n3.1. REGISTRAR EXPERT TRAINER DEL GRUPO INTERMEDIO\n3.2. BÚSQUEDA DE CAMPERS DUPLICADOS\n3.3. ELIMINACION DE CAMPERS POR INASISTENCIA\n3.4. LISTAR CAMPERS\n3.5. TRANSLADO DE CAMPER ENTRE GRUPOS POR NIVELACION\n3.6. AGREGAR CAMPERS AL GRUPO (despues del registro inicial)\n3.7. REPORTAR CAMPERS DE MAYOR Y MENOR EDAD\n"))

    if opcion == 3.0:
        createGroup(3)
    elif opcion == 3.1:
        None
    elif opcion == 3.2:
        None
    elif opcion == 3.3:
        None
    elif opcion == 3.4:
        None
    elif opcion == 3.5:
        None
    elif opcion == 3.6:
        None
    elif opcion == 3.7:
        None


def addTrainer (categoria):
    nombre = input("Ingrese el nombre del Trainer:\t")
    ingreso = input("Fecha de ingreso: (dd/mm/aaaa)\t")
    edad = int(input("edad:\t"))
    categoria[0].append({"nombre":nombre,"ingreso":ingreso,"edad":edad})

def addStudent(categoria):
        nombre = input("Ingrese el nombre del alumno:\t")
        ingreso = input("Fecha de ingreso: (dd/mm/aaaa)\t")
        grupo = input("Grupo:\t")
        edad = int(input("edad:\t"))
        categoria[1].append({"nombre":nombre,"ingreso":ingreso,"grupo":grupo,"edad":edad})

def createGroup(nivel):
    if nivel == 1:
        basico = [[],[]]
        cantAlumnos = int(input("Ingrese la cantidad de alumnos a añadir el grupo BÁSICO"))
        for alumno in range(cantAlumnos):
            addStudent(basico)
        CAMPUS.insert(0,basico)
    if nivel == 2:
        intermedio = [[],[]]
        cantAlumnos = int(input("Ingrese la cantidad de alumnos a añadir el grupo INTERMEDIO"))
        for alumno in range(cantAlumnos):
            addStudent(basico)
        CAMPUS.insert(1,intermedio)
    if nivel == 3:
        avanzado = [[],[]]
        cantAlumnos = int(input("Ingrese la cantidad de alumnos a añadir el grupo AVANZADO"))
        for alumno in range(cantAlumnos):
            addStudent(avanzado)
        CAMPUS.insert(2,avanzado)

menu()
print(CAMPUS)