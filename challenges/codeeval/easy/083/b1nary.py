#python 2.7
import collections
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test =  test.replace('\n', '').lower()
    frequency = collections.Counter(test)
    values = []
    for letter,n in frequency.iteritems():  #saving only the values of the letters
        if letter.isalpha():
            values.append(n)
    solve = 0
    beauty = 26
    values.sort(reverse=True) #sorting descending 
    for i in values:
        solve+= beauty*i
        beauty= beauty-1
    print solve
    
test_cases.close()
