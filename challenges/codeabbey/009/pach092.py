datos = int(raw_input())
for triangulos in range(datos):
    valores = raw_input().split()
    mayor = max(int(valores[0]),int(valores[1]),int(valores[2]))
    valores.remove(str(mayor))
    a, b = int(valores[0]), int(valores[1])
    c = mayor
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print 1 
        print " "
    elif (a + b) == c:
        print 1
        print " "
    else:
        print 0
        print " "
