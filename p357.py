from math import sqrt

primefile = open("primes1.txt")
primelist = []
for line in primefile:
    currprimes = [int(val) for val in line.strip().split()]
    for currprime in currprimes:
        primelist.append(currprime)

def isprime(value):
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

def divisors(n):
    divli = [1]
    i=2
    while i<sqrt(n):
        if n%i==0:
            divli.append(i)
        i+=1
    if sqrt(n)==int(sqrt(n)):
        divli.append(int(sqrt(n)))
    return divli

goods = []
for i in range(2,1000,4):
    isgood = True
    for elem in divisors(i):
        if not isprime(elem + i//elem):
            isgood = False
            print(i, elem)
    if isgood:
        goods.append(i)
print(goods)