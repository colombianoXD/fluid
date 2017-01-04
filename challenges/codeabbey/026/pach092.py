datos = int(raw_input())
respuesta = []
for operaciones in range(datos):
    valores = map(int, raw_input().split())
    temporal = valores[0] * valores[1]
    while valores[0] != valores[1]:
        valores.sort()
        valores[1] = valores[1] - valores[0]
    mcd = valores[0]
    mcm = temporal / mcd
    respuesta.append('('+str(mcd)+' '+str(mcm)+')')
print(' '.join(respuesta))
