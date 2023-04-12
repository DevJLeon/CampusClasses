string ="Cualquier Cosaaaaaoouu"

voc=[[0],[0],[0],[0],[0]]

for i in string:
    if i == "a":
        voc[0].append(1)
    elif i == "e":
        voc[1].append(1)
    elif i == "i":
        voc[2].append(1)
    elif i == "o":
        voc[3].append(1)
    elif i == "u":
        voc[4].append(1) 
    else: continue
    
print("cantidad de a:", sum(voc[0]),"\ncantidad de e:", sum(voc[1]),"\ncantidad de i:", sum(voc[2]),"\ncantidad de o:", sum(voc[3]),"\ncantidad de u:", sum(voc[4]))