juego = {
    "p1":{
        "nombre":"",
        "puntos":0
    },
    "p2":{
        "nombre":"",
        "puntos":0
    }
}
## juego["p1"]["nombre"] = "Juan Alberto"
## juego["p1"]["puntos"] = int(input("Ingrese los puntos de Juan Alberto: "))

juego["p1"] = {"nombre": "Juan Alberto", "puntos":20}

for i in range (2,5):
    juego["p"+(str(i))] = {
        "nombre":input("Ingrese el nombre del jugador p"+str(i)+": "),
        "puntos":int(input("Ingrese los puntos: "))
    }

print(juego)