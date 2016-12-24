nVal = raw_input()

response = ''
for i in range(int(nVal)):
	a,b,vals = raw_input().split()
	
	total = 0
	for num in range(int(vals)):
		total = total +(int(a)+(num*int(b)))
	response = response + '%d ' %total
	

print response
