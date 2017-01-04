checksum=[3, 1, 4, 1, 5, 9]
checksum=[int(x) for x in checksum]
respuesta=0
multiplicar=113
modulo=10000007
for x in range(len(checksum)):
    respuesta=((respuesta+checksum[x])*multiplicar)%modulo
print(respuesta)
