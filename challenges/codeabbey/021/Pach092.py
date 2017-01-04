m = [1, 2, 3, 2, 3, 1, 1, 1, 1, 3]
cantidad = len(m)
n = input("ingresa n: ")
a = 0
contador = range(1, n + 1)
contador_0 = []
prueba = ""
cantidad_contador = len(contador)
while a < cantidad_contador:
	contador_nuevo = contador[a] - (a + 1)
	a += 1
	contador_0.append(int(contador_nuevo))
	prueba = contador_0
for i in range(0, cantidad):
	x = int(m[i] - 1)
	prueba[x] = int(prueba[x] + 1)
for respuesta in str(prueba).split(","):
	print respuesta
