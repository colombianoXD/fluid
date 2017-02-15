"""This script contains strings rotated in accordance
with the rule above, separated by spaces. For example:"""
CANTIDAD = int(raw_input())
RESPUESTA = []
for reto in range(CANTIDAD):
    datos = raw_input().split()
    rotacion = int(datos[0])
    resultado = datos[1][rotacion:] + datos[1][:rotacion]
    RESPUESTA.append(resultado)
print ' '.join(RESPUESTA)
