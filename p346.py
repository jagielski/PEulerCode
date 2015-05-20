MAX = 10**12
k=2
count = 1
already = set()
while k**2+k+1<MAX:
    print(k)
    value = k*k+k+1
    power = 3
    while value<MAX:
        if not value in already:
            already.add(value)
            count+=value
        value+=k**power
        power+=1
    k+=1
print(count)