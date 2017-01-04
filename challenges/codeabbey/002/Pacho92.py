sumar = [10, 20, 30, 40, 5, 6, 7, 8]
def lista(numeros):
	suma = 0
	for i in numeros:
		suma = suma + i
	return suma
print 'la suma de',sumar,'es',(lista(sumar))
