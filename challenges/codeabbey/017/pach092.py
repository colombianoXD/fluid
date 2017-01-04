multiplicar = 113
dividir = 10000007
respuesta = 0
datos = int(raw_input())
checksum = raw_input().split()
for a in checksum:
  respuesta = (respuesta + int(a))*multiplicar
print(respuesta % dividir)
