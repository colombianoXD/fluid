fahrenheit = [495, 353, 168, -39, 22]
cantidad = len(fahrenheit)
a = 0
respuesta = []
while a < cantidad:
	celsius = float(fahrenheit[a])
	celsius = int(round(float((celsius)-32)*(0.555556)))
	respuesta.append(str(celsius))
	print (' '.join(respuesta))
	a += 1
