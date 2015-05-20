for denom in range(10,99):
    for i in range(1,denom//10):
        numer = i*10+denom//10
        if numer*(denom%10)==denom*i:
            print(numer, denom)