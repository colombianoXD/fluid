coinciden = """(a+[b*c]-{d/3})
(a + [b * c) - 17]
(((a * x) + [b] * y) + c
auf(zlo)men [gy<psy>] four{s}""".split("\n")
for a in range(len(coinciden)):
    x = coinciden[a]
    y = 1
    z = 1
    parentesis = 0
    corchetes = 0
    llaves = 0
    mayor_menor = 0
    for k in range(len(x)):
        if x[k] == "(":
            parentesis += y
            z = y
            y *= 2
        elif x[k] == "{":
            llaves += y
            z = y
            y *= 2
        elif x[k] == "[":
            corchetes += y
            z = y
            y *= 2
        elif x[k] == "<":
            mayor_menor += y
            z = y
            y *= 2
        elif x[k] == ")":
            parentesis -= z
            z /= 2
            y /= 2
            if parentesis < 0:
                break
        elif x[k] == "}":
            llaves -= z
            z /= 2
            y /= 2
            if llaves < 0:
                break
        elif x[k] == "]":
            corchetes -= z
            z /= 2
            y /= 2
            if corchetes < 0:
                break
        elif x[k] == ">":
            mayor_menor -= z
            z /= 2
            y /= 2
            if mayor_menor < 0:
                break
    if parentesis == 0 and mayor_menor == 0 and llaves == 0 and corchetes == 0:
        print "1"
    else:
        print "0"
