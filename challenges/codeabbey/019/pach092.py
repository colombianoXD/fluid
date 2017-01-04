abren = ['(' , '[' , '{' , '<']
cierran = [')' , ']' , '}' , '>']
datos = int(raw_input())
respuesta = []
for a in range (datos) :
    cadena = list(raw_input())
    comprueba = []
    resultado = 1
    for i in cadena :
        if i in abren :
            comprueba.append(i)
        elif i in cierran :
            ind = cierran.index(i)
            if comprueba == [] :
                resultado = 0
            elif comprueba[-1] == abren[ind] :
                comprueba = comprueba[0:len(comprueba)-1]
            else :
                resultado = 0
    if comprueba != [] : resultado = 0
    respuesta.append(str(resultado))
print(' '.join(respuesta))
