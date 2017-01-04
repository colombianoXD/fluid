datos = """2 3 7 0
20 10 0
1 0"""
cadena = datos.split("\n")
def promedio(array):
    total = 0
    for datos in range(0, len(array) - 1):
        total += int(array[datos])    
    promedio = total / float(len(array) - 1)
    print int(round(promedio))    
for x in cadena:
    a = [int(datos) for datos in x.split(" ")]
    promedio(a)
