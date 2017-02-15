"""This script contains the number of person who will
remain at the end. Initial numbering starts from 1."""
DATOS = raw_input().split(' ')
N, K = int(DATOS[0]), int(DATOS[1])
RESULTADO = 0
i = 1
while i <= N:
    RESULTADO = (RESULTADO + K) % i
    i += 1
print RESULTADO + 1
