miLista = [{"nombre": "Patricio","edad":21},{"nombre":"Juan", "edad":18},{"nombre":"Juan", "edad":38},{"nombre":"Juan", "edad":8}]

miTupla = (1,2,3)

m = len(miLista)

for i in range(m-1):
    for j in range (i+1,m):
        if miLista[i]["edad"]>miLista[j]["edad"]:
            t = miLista[i]["edad"]
            miLista[i]["edad"] = miLista[j]["edad"]
            miLista[j]["edad"]=t
        
print(miLista)