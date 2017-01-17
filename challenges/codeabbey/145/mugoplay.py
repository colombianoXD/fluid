"""Modular Exponentiation """


def modulus_calculation(bin_ex, fst_modulus, input_vector):
    """Calculo del modulo"""
    counter = 1
    len_bin = len(bin_ex)

    while counter < len_bin:
        if bin_ex[counter] == "1":
            fst_modulus = (
                (fst_modulus**2)*(int(input_vector[0]))) % int(input_vector[2])
        else:
            fst_modulus = ((fst_modulus)**2) % int(input_vector[2])
        counter += 1

    return fst_modulus


def create_members(file):
    """Creando miembros de la ecuacion"""
    with open(file, "r") as input_list:
        for lst in input_list.readlines():
            lst = lst.strip()
            input_vector = lst.split(" ")
            bin_ex = format(int(input_vector[1]), "b")
            fst_modulus = (
                (1**2)*(int(input_vector[0]))) % int(input_vector[2])
            modulus_result = modulus_calculation(
                bin_ex, fst_modulus, input_vector)

            print modulus_result


create_members("DATA.txt")
