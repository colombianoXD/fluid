datos=int(raw_input())
for(redondeo)in range(datos):
    valores=raw_input().split()
    a,b=float(valores[0]),float(valores[1])
    res=a/b
    respuesta=round(res)
    print(str(int(respuesta))+" ")
