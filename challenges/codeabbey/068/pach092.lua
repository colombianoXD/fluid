amount = io.read("*n")
answer = {}
for i = 1, amount do
    d, a, b = io.read("*n", "*n", "*n")
    table.insert(answer, (a * ((d - 0) / (a + b))))
end
io.write(table.concat(answer, " "))
