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
    
def istruncleft(prime):
    if prime in primelist[0:4]:
        return True
    left = int(str(prime)[1:])
    if isprime(left):
        return istruncleft(left)
    else:
        return False
        
def istruncright(prime):
    if prime in primelist[0:4]:
        return True
    right = prime//10
    if isprime(right):
        return istruncright(right)
    else:
        return False

def istrunc(prime):
    return istruncright(prime) and istruncleft(prime)
        
truncprimes = []

for prime in primelist[4:]:
    if istrunc(prime):
        truncprimes.append(prime)
        print(prime)
for value in range(100000,1000000):
    if value%100000 == 0:
        print("Current:", value)
    if isprime(value):
        if istrunc(value):
            truncprimes.append(value)
            print(value)
        
print(len(truncprimes),truncprimes, sum(truncprimes))