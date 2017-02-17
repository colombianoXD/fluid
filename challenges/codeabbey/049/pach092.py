"""should for each of matches specify whether first player wins
(by value 1) or second (by value 2). There would be no draws."""
AMOUNT = input()
for i in range(int(AMOUNT)):
    ar = raw_input().split()
    v1, v2 = 0, 0
    for j in ar:
        if j in ('RS', 'SP', 'PR'):
            v1 += 1
        if j in ('SR', 'PS', 'RP'):
            v2 += 1
    if v1 > v2:
        print '1 '
    else:
        print '2 '
