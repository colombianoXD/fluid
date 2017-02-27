amount = io.read("*n")
for i = 1, amount do
    fibonacci = {0, 1, 1}
    number = io.read("*n")
    a = 2
    add = 0
    while add < number do
        add = fibonacci[a] + fibonacci[a + 1]
        table.insert(fibonacci, add)
        a = a + 1
    end
    if number == 0 then
        a = 0
    end
    print(a)
end
