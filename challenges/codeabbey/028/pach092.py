datos = int(raw_input())
respuesta = []
for a in range(datos):
    valores = [float(x) for x in raw_input().split(" ")]
    IMC = float(valores[0]/(valores[1]**2))
    if IMC < 18.5:
	    respuesta.append(str('under'))
    elif IMC < 25.0:
	    respuesta.append(str('normal'))
    elif IMC < 30.0:
	    respuesta.append(str('over'))
    else:
	    respuesta.append(str('obese'))
print (' '.join(respuesta))
