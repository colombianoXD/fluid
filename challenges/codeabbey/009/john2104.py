#http://www.wikihow.com/Find-the-Height-of-a-Triangle
def calcS(a,b,c):
	return (a+b+c)/2
def calcSqrt(a,b,c,s):
	return s*((s-a)*(s-b)*(s-c))
def main():
	nVal = raw_input()
	response = ''
	for i in range(int(nVal)):
		a,b,c = raw_input().split()
		
		s = calcS(int(a),int(b),int(c))
		sq = calcSqrt(int(a),int(b),int(c),s)
		
		if sq > 0:
			response = response + '1 '
		else:
			response = response + '0 '
	print response
main()
