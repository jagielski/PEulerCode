from itertools import permutations
perms = [int(''.join(p)) for p in permutations('7654321')]
primefile = open("primes1.txt")
primelist = []
i=0
for line in primefile:
    currprimes = [int(val) for val in line.strip().split()]
    for currprime in currprimes:
        if currprime%4==1:
            primelist.append(currprime)
    i+=1

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
for value in perms:
    if isprime(value):
        print(value)
        exit(0)