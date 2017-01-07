datos=int(raw_input())
for(progresion)in range(datos):
    valores=map(int,raw_input().split())
    a,b,n=int(valores[0]),int(valores[1]),int(valores[2])
    total=0
    for(x)in range(n):
       total=(a+(b*x))+total
    print(str(total)+' ')
