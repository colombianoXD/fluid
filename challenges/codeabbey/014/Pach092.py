operaciones = """5
+ 3
* 7
+ 10
* 2
* 3
+ 1
% 11"""
def modular(x, y, z):
  eval(x + y + z)
y = True
for secuencial in operaciones.split('\n'):
  if y:
    respuesta = secuencial
    y = False
  else:
    respuesta = eval(str(respuesta)+secuencial)
print respuesta
