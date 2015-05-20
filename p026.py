primefile = open("primesunderthousand.txt")
primelist = []
for line in primefile:
    primelist.append(int(line.strip()))
primelist.remove(2)
primelist.remove(5)
def cyclelength(prime):
    foundcycle = False
    i=1
    while not foundcycle:
        if (10**i - 1)%prime == 0:
            return i
        i += 1

print(cyclelength(3),cyclelength(7), cyclelength(53))

cyclelist = []
for prime in primelist:
    cyclelist.append((prime, cyclelength(prime)))
    print(prime, cyclelength(prime))
    
curlongest = 1
curprime = 3
for pair in cyclelist:
    if pair[1]>curlongest:
        curprime = pair[0]
        curlongest = pair[1]
print(curprime, curlongest)