datos = gets
datos = datos.split(' ').map(&:to_i)
n = datos[0]
k = datos[1]
datos = []
n.times do |i|
  datos[i] = i + 1
end
i = 0
contador = 1
while datos.length != 1
  if contador == k
    datos.delete_at(i)
    contador = 0
    i -= 1
  end
  if i >= datos.length - 1
    i = 0
  else
    i += 1
  end
  contador += 1
end
print datos[0].to_s
