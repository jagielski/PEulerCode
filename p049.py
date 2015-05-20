f = open("primes-to-100k.txt")
validprimes = []
currline = int(f.readline().strip())
while currline<10000:
    if currline>1000:
        validprimes.append(currline)
    currline = int(f.readline().strip())
print(validprimes)

diff = 0
for i in range(250):
    print(i)
    diff += 18
    index = 0
    prime = validprimes[index]
    while prime < 10000-2*diff:
        if ((prime + diff) in validprimes) and ((prime+2*diff) in validprimes):
            if sorted(str(prime))==sorted(str(prime+diff)) and sorted(str(prime))==sorted(str(prime+2*diff)):
                print("Progression:", [prime, prime+diff, prime+2*diff])
        index += 1
        prime = validprimes[index]
