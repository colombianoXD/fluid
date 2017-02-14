cantidad = gets.chomp.to_i
resultado = []
cantidad.times do
  (k, s) = gets.chomp.split
  k = k.to_i
  longitud = s.length
  if k < 0
    indice = (longitud - 1) * k.abs
    j = 1
    indice_final = 0
  else
    indice = 0
    j = -1
    indice_final = (longitud - 1) * k
  end
  until indice == indice_final
    t = s[(indice + j) % longitud]
    s[(indice + j) % longitud] = s[indice % longitud]
    s[indice % longitud] = t
    indice -= j
  end
  resultado << s
end
puts resultado.join(' ')
