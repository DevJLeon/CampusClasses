##Determinar en los meses de abril, mayo, junio el promedio de lluvias al mes, teniendo en cuenta los centìmetros de lluvia caìdos por dìa. (los velores de
##los cms de lluvia por dìa pueden ser generados por medio de un nùmero aleatorio entre 0 y 11) determinar cuàl fue el mes màs lluvioso en promedio

import random

dias = 30
abril = []
mayo = []
junio = []

for i in range (dias):
    abril.append(random.randint(0,11))
    mayo.append(random.randint(0,11))
    junio.append(random.randint(0,11))

promedioAbril = sum(abril)/30
promedioMayo = sum(mayo)/30
promedioJunio = sum(junio)/30

if promedioAbril > promedioMayo and promedioAbril > promedioJunio:
    print("El mes con mayor promedio de lluvias fue Abril, siendo este: " + str(promedioAbril), "\n y esta serìa la tabla de lluvias:  y esta serìa la tabla de lluvias: " , )
    for j in range(dias):
        print(abril[j], end = ", ")
elif promedioMayo > promedioAbril and promedioMayo > promedioJunio:
    print("El mes con mayor promedio de lluvias fue Mayo, siendo este: " + str(promedioMayo), "\n y esta serìa la tabla de lluvias: ")
    for k in range(dias):
        print(mayo[k], end = ", ")
else:
    print("El mes con mayor promedio de lluvias fue Junio, siendo este: " + str(promedioJunio), "\n y esta serìa la tabla de lluvias: ")
    for l in range(dias):
        print(junio[l], end = ", ")