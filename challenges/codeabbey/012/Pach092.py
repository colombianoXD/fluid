fechas = [1,0,0,0,2,3,4,5,5,3,23,22,24,4,20,45,8,4,6,47,9,11,51,13]
cantidad = len(fechas)
z = 0
respuesta = []
while z < cantidad:
	d1, h1, m1, s1 = int(fechas[z]), int(fechas[z + 1]), int(fechas[z + 2]), int(fechas[z + 3])
	d2, h2, m2, s2 = int(fechas[z + 4]), int(fechas[z + 5]), int(fechas[z + 6]), int(fechas[z + 7])
	if s1 <= s2:
		s = s2 - s1
	else:
		m2 -= 1
		s2 += 60
		s = s2 - s1
	if m1 <= m2:
		m = m2 - m1
	else:
		h2 -= 1
		m2 += 60
		m = m2 - m1
	if h1 <= h2:
		h = h2 - h1
	else:
		d2 -= 1
		h2 += 24
		h = h2 - h1
	if d1 <= d2:
		d = d2 - d1
	else:
		print 'Error en fechas'
	respuesta.append('('+str(d)+' '+str(h)+' '+str(m)+' '+str(s)+') ')
	print(' '.join(respuesta))
	z += 8
