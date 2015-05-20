import numthy

primefile = open("primes100m.txt")
primelist = []
for line in primefile:
    primelist.append(int(line.strip()))
print(primelist[-1])
totalcount = 0
i=0
for prime in primelist[2:]:
    if prime>i*1000000:
        print(i*1000000)
        i+=1
    last = (prime-1)/2
    count = last
    a = numthy.solvelincong(-3,last,prime)
    count += a
    b = numthy.solvelincong(-4,a,prime)
    count += b
    count = count % prime
    totalcount += count
print(totalcount)