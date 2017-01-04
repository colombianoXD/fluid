datos = [2, 3, 4, 10]
cantidad = len(datos)
x = 0
respuesta = []
def mcm(a,b):
        return(a * b / mcd(a, b))
        
def mcd(a,b):
        while b:      
                a, b = b, a % b
        return a
while x < cantidad:
	a, b = int(datos[x]), int(datos[x + 1])
	respuesta.append('('+str(mcd(a,b))+' '+str(mcm(a,b))+')')
	print(' '.join(respuesta))
	x += 2
