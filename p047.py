from math import sqrt

primefile = open("primes100m.txt")
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

    
def primefactors(number):
    if isprime(number):
        factset = set()
        factset.add(number)
        return factset
    else:
        index = 0
        while primelist[index] <= sqrt(number):
            if number%primelist[index]==0:
                factset = primefactors(number/primelist[index])
                factset.add(primelist[index])
                return factset
            index += 1
            
factorlens = [0,0]
for i in range(2,200000):
    if i%20000==0:
        print("Factoring:", i)
    factorlens.append(len(primefactors(i)))
    
count = 4
for j in range(len(factorlens)-(count-1)):
    if j%20000==0:
        print("Diffs:",j)
    if factorlens[j] == count:
        allcount = True
        for i in range(count):
            if factorlens[j+i]!=factorlens[j]:
                allcount = False
        if allcount:
            print([j+i for i in range(count)])
            exit(0)