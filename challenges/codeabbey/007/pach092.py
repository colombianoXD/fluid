celcius=raw_input().split()
fahrenheit=0
for(temperatura)in celcius[1:]:
    fahrenheit=int(round((float(temperatura)-32)*5/9))
    print(str(fahrenheit)+' ')
