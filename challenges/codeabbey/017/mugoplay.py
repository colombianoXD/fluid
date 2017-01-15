"""Array Checksum"""

string_vector = "819091408 655102071 13 38536125 349 31992 6500990 1811 8287332"
elements_vector = string_vector.split(" ")
result = 0
for n in elements_vector:
    result += int(n)
    result = result*113
    result = result % 10000007
print result
