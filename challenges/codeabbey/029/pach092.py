lista = list((int(i) for i in raw_input().split()))
cantidad = len(lista)
informacion = dict()
fin = len(lista)-1
for i in range (cantidad):
    informacion[i] = lista[i]
while (fin != -1):
    pasar = -1
    for i in range (0,fin):
        if lista[i] > lista[i + 1]:
            temporal = lista[i]
            lista[i] = lista[i+1]
            lista[i + 1] = temporal
            pasar = i
    fin = pasar
respuesta = ''
for i in lista:
    for j in range (len(lista)):
        if i == informacion[j]:
            respuesta += str(j + 1) + ' '
print(respuesta)
