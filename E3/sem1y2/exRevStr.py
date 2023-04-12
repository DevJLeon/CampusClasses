def reverse(string):
    rstr = ""
    length = len(string)
    for i in range(length):
        rstr += string[length-1]
        length -= 1
    return rstr

print(reverse("Hola, probando, si, sonido."))