cantidad = gets.chomp.to_i
datos = gets.chomp.split.map(&:to_i)
resultado = []
(0...cantidad).each do |a|
  contador = 0
  truncados = []
  numero = datos[a]
  until truncados.include? numero
    truncados << numero
    contador += 1
    numero = (numero * numero) / 100 % 10_000
  end
  resultado << contador
end
puts resultado.join(' ')
