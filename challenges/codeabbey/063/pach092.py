"""This script contains product representation for each
of these integers, written like p1*p2*p3 where p1 ... p3
are some primes sorted in non-decreasing order."""
AMOUNT = input()


def operacion():
    """This def makes the operations"""
    numbers = int(raw_input())
    __a__ = 2
    while numbers != 1:
        if numbers % __a__ == 0:
            numbers = numbers / __a__
            if numbers == 1:
                print str(__a__) + " "
            else:
                print str(__a__) + "*"
        else:
            __a__ += 1


for x in range(0, int(AMOUNT)):
    operacion()
