import itertools
import sys

def triangle(rows):
    """ Modified function to build the pascal triangle, taken from
        http://stackoverflow.com/questions/3134813/pascals-triangle-in-python
    """
    newlist =[]
    for rownum in range (rows):
        newValue=1
        PrintingList = [newValue]
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        newlist.append(PrintingList)
    return newlist
    
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num = int(test.strip())
        if test.strip() != "":
            total = list(itertools.chain.from_iterable(triangle(int(num))))
            print " ".join([str(number) for number in total])