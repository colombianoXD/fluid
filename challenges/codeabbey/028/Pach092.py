datos = [80, 1.73, 55, 1.58, 49, 1.91]
cantidad = len(datos)
respuesta = []
a = 0
while a < cantidad:
	peso, altura = float(datos[a]), float(datos[a + 1])
	IMC = float (peso / (altura * altura))
	if IMC < 18.5:
		respuesta.append(str('under'))
	elif IMC >= 18.5 and IMC < 25.0:
		respuesta.append(str('normal'))
	elif IMC >= 25.0 and IMC < 30.0:
		respuesta.append(str('over'))
	elif IMC >= 30.0:
		respuesta.append(str('obese'))
	print (' '.join(respuesta))
	a += 2
