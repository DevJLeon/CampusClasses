##15-30-40

puntosJ = 0
puntosO = 0

setJ = 0
setO = 0

while puntosJ <=15 or puntosO <= 15:

    pointCounter = input("Indique quién anotó el punto. Escriba J para Juan, O para Octavio: ").upper()

    if pointCounter == "J":
        puntosJ += 1
    elif pointCounter == "O": 
        puntosO += 1

    print(puntosJ, puntosO)

    if puntosJ == 15 or puntosJ == 30 or puntosJ == 40:
        setJ += 1
        print("Juan gana el set. Puntuación", setJ, "a", setO)
                
    elif puntosO == 15 or puntosO == 30 or puntosO == 40:
        setO += 1
        print ("Octavio gana el set. Puntuación", setJ, "a", setO)

    if setO == 2 or setJ == 2:
        break

if setJ > setO:
    print("\n****************************************************\nEl ganador del juego es Juan con Puntuación", puntosJ, "a", puntosO, "\n****************************************************\n")
else: 
    print("\n****************************************************\nEl ganador del juego es Octavio con Puntuación", puntosO, "a", puntosJ, "\n****************************************************\n")

print("\n\nJuego finalizado\n\n")
    
        
