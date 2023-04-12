## Nombre de los estudiantes y sus notas para el primer corte, segundo y tercero. calcular definitiva.

cantidadAlumnos = int(input("Ingrese la cantidad de estudiantes: "))
db = []

### forma fàcil
###
###for i in range(cantidadAlumnos):
###    nombre = input("Ingrese el nombre del estudiante: ")
###    nota1 = float(input("Ingrese la nota del primer corte: "))
###    nota2 = float(input("Ingrese la nota del segundo corte: "))
###    nota3 = float(input("Ingrese la nota del tercero corte: "))
###    nota = (nota1 + nota2 + nota3) / 3
###    print(f"La nota de {nombre} es {nota}.")
###

## "\033[1m" + 
## Matrices

for i in range(cantidadAlumnos):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la nota del primer corte: "))
    nota2 = float(input("Ingrese la nota del segundo corte: "))
    nota3 = float(input("Ingrese la nota del tercero corte: "))
    nota = (nota1 + nota2 + nota3) / 3
    db.append([nombre, nota, nota1,nota2,nota3])
for j in range(cantidadAlumnos):
    print("Las notas del alumno", str(db[j][0]) + ", son", str(db[j][2]) + ", ", str(db[j][3])+", ", str(db[j][4])+".", "Con promedio:", "\033[1m" + str(db[j][1]))

