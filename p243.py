from math import sqrt

primefile = open("primes-to-100k.txt")
primelist = []
for line in primefile:
    primelist.append(int(line.strip()))

def isprime(value):
    if value<=primelist[-1]:
        low = 0
        high = len(primelist)
        mid = (low + high) // 2
        while (low<=high):
            mid = (low + high) // 2
            midval = primelist[mid]
            if midval == value:
                return True
            elif midval < value:
                low = mid + 1
            else:
                high = mid - 1
        return False
    else:
        index = 0
        while primelist[index]<=sqrt(value):
            if value%primelist[index] == 0:
                return False
            index+=1
        return True

primefactorlist = [[frozenset(),frozenset()]]
listlens = 10000
for i in range(20):
    primefactorlist.append([])

def primefactors(number):
    if isprime(number):
        factset = set()
        factset.add(number)
        primefactorlist[number//listlens].append(frozenset(factset))
        return factset
    else:
        index = 0
        while primelist[index] <= sqrt(number):
            if number%primelist[index]==0:
                newindex = number//primelist[index]
                factset = set(primefactorlist[newindex//listlens][newindex%listlens])
                factset.add(primelist[index])
                primefactorlist[number//listlens].append(frozenset(factset))
                return factset
            index += 1
            
def totient(number):
    curr = number
    primeset = primefactors(number)
    for prime in primeset:
        curr*=((prime-1)/prime)
    return (curr)

# curmin = 1
# for i in range(2,200000):
    # if (i%100000==0):
        # print(i)
    # a=totient(i)
    # if a/(i-1)<curmin:
        # print("New min:",i,a, primefactorlist[i//listlens][i%listlens])
        # curmin = a/(i-1)
    # if a/(i-1)<(15499/94744):
        # print("Final result:", i)
        # exit(0)
    
ultimate = 15499/94744
curallprimes = []
for i in range(10):
    product = 1
    divisor = 1
    for j in range(i+1):
        product*=primelist[j]
        divisor *= (primelist[j]-1)/primelist[j]
    print(product, divisor)
    comp = 1
    while comp < primelist[i+1]:
        newval = comp*product
        print("New min:", newval)
        if (newval*divisor)/(newval-1)<ultimate:
            print("Final result:", newval)
            exit(0)
        comp+=1