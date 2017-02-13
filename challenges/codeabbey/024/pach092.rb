=begin
This script contains number of iterations for sequences with such initial
values to come to the loop.
=end
cantidad = gets.chomp.to_i
datos = gets.chomp.split.map(&:to_i)
resultado = []
for a in (0...cantidad)
  contador = 0
  truncados = []
  numero = datos[a]
  until truncados.include? numero
    truncados << numero
    contador += 1
    numero = (numero * numero) / 100 % 10000
  end
  resultado << contador
end
puts resultado.join(' ')
