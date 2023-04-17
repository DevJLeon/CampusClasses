miLista = ["Juan", "Maria", "José", "Tulio", "Armando"]

miTupla = (1,2,3)

miLista.sort(reverse=True)

m = len(miLista)

for i in range(m-1):
    for j in range (i+1,m):
        if miLista[i]>miLista[j]:
            t = miLista[i]
            miLista[i] = miLista[j]
            miLista[j]=t
        
print(miLista)