estudiantes = ["Carlos", "Domingo", "Laura", "Luna", "Miguel"]
num = [[1,2,3], [5,6,7]]

##print(estudiantes[1], "\n")
##print(num[1][1], "\n")

##for i in range(3):
##    print(num[0][i], end=" ")
##print("\n")
##for j in range(3):
##    print(num[1][j], end = " ")

for i in range(2):
    fila = ""
    for j in range(3):
        fila = str(num[i][j])
        print(fila)