from datetime import date

def addPacient():
    codigo = len(pacientes)+1
    name = input("Ingrese el nombre del paciente: \t")
    bDay = input("Ingrese la fecha de nacimiento del paciente: (dd/mm/aaaa) \t")
    age = bDay.split("/")
    age = calculateAge(date(int(age[2]),int(age[1]),int(age[0])))
    weight = float(input("Ingrese el peso del paciente en kg: \t"))
    gender = int(input("Indique el sexo del paciente \n 0. Masculino 1.Femenino: \t"))
    if gender == 0:
        gender = "Masculino"
    elif gender == 1:
        gender = "Femenino"
    pacientes.append({"codigo":codigo,"nombre":name,"fechaNacimiento":bDay,"edad":age,"peso":weight,"sexo":gender})
    return(pacientes)

def showPacients():
    list = "CODIGO \t NOMBRE \t FECHA NACIMIENTO \t EDAD \t PESO \t SEXO \n"
    for paciente in range(len(pacientes)):
        list += (str(pacientes[paciente]["codigo"])+ "   \t"+str(pacientes[paciente]["nombre"])+ "   \t"+str(pacientes[paciente]["fechaNacimiento"])+"   \t \t "+str(pacientes[paciente]["edad"])+ "   \t"+str(pacientes[paciente]["peso"])+ "   \t"+str(pacientes[paciente]["sexo"])+ "\n")
    print(list)
    
def editPacient():
    showPacients()
    id = int(input("Ingrese el codigo del paciente a editar: \t"))
    if id > len(pacientes) or id <= 0:
        print("\n\n****************Paciente no encontrado. Por favor Inténtelo de nuevo****************\n\n")
        id = int(input("Ingrese el codigo del paciente a editar: \t"))
    cambios = int(input("¿Qué desea cambiar? \n 1. Nombre \t 2. Fecha Nacimiento \n 3. Peso \t 4. sexo \n 0. Nada(volver)"))
    while cambios != 0:
        if cambios == 1:
            nombre = input("Ingrese el nombre del paciente: \t")
            pacientes[id-1]["nombre"]=nombre
        elif cambios == 2:
            nacimiento = input("Ingrese la fecha de nacimiento del paciente: (dd/mm/aaaa) \t")
            pacientes[id-1]["fechaNacimiento"]=nacimiento
        elif cambios == 3:
            peso = float(input("Ingrese el peso del paciente en kg: \t"))
            pacientes[id-1]["peso"]=peso
        elif cambios == 4:
            genero = int(input("Indique el sexo del paciente \n 0. Masculino 1.Femenino: \t"))
            if genero == 0:
                genero = "Masculino"
            elif genero == 1:
                genero = "Femenino"
            pacientes[id-1]["sexo"]=genero
        cambios = int(input("¿Qué desea cambiar? \n 1. Nombre \t 2. Fecha Nacimiento \n 3. Peso \t 4. sexo \n 0. Nada(volver)"))
    return(pacientes)
    
def deleteInfo():
    showPacients()
    id = int(input("Ingrese el codigo del paciente a editar: \t"))
    if id > len(pacientes) or id <= 0:
        print("\n\n****************Paciente no encontrado. Por favor Inténtelo de nuevo****************\n\n")
        id = int(input("Ingrese el codigo del paciente a editar: \t"))
    cambios = int(input("¿Qué desea eliminar? \n 1. Nombre \t 2. Fecha Nacimiento \n 3. Peso \t 4. sexo \n 0. Nada(volver)"))
    while cambios != 0:
        if cambios == 1:
            nombre = "N/A"
            pacientes[id-1]["nombre"]=nombre
        elif cambios == 2:
            nacimiento = "N/A"
            pacientes[id-1]["fechaNacimiento"]=nacimiento
        elif cambios == 3:
            peso = "N/A"
            pacientes[id-1]["peso"]=peso
        elif cambios == 4:
            genero = "N/A"
            pacientes[id-1]["sexo"]=genero
        cambios = int(input("¿Qué desea cambiar? \n 1. Nombre \t 2. Fecha Nacimiento \n 3. Peso \t 4. sexo \n 0. Nada(volver)"))
    return(pacientes)
        
def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age

pacientes = []

opcion = 1
while opcion != 0:
    opcion = int(input("Seleccione alguna de las siguientes opciones:\n1.Crear nuevo paciente \t \t \t2.Editar datos de un paciente\n3.Borrar datos de un paciente \t \t 4.Listar todos los pacientes \n0. Salir: \t"))
    if opcion == 1:
        addPacient()
    elif opcion == 2:
        editPacient()
    elif opcion == 3:
        deleteInfo()
    elif opcion == 4:
            showPacients()


