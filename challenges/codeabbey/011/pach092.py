datos=int(raw_input())
for(sumatoria)in range(datos):
    valores=raw_input().split()
    a,b,c=int(valores[0]),int(valores[1]),int(valores[2])
    total=list(str(((a*b)+c)))
    suma=0
    for(resultado)in(total):
        suma+=int(resultado)
    print(str(suma)+' ')
