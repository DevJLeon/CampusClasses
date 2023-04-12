temperaturaF = float(input("Ingrese la temperatura en grados Farenheigh: "))

def ConvertirTemperatura(temperaturaF):
    temperaturaC = (temperaturaF-32)*(5/9)
    return(print("La temperatura en grados celcius es", temperaturaC, "°"))

ConvertirTemperatura(temperaturaF)

