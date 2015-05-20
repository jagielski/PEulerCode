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

ulamlist = [1]
for i in range(1,30000,2):
    ulamlist.append(i**2+i+1)
    ulamlist.append(i**2+2*i+2)
    ulamlist.append(i**2+3*i+3)
    ulamlist.append(i**2+4*i+4)
print("a")
ulamsum = [0]
for i in range(1,len(ulamlist)):
    newval = 0
    if isprime(ulamlist[i]):
        newval = 1
    ulamsum.append(ulamsum[i-1]+newval)
print("b")
print(ulamsum[13]/13)
for i in range(3,30000,2):
    if ulamsum[2*i-1]/(2*i-1)<0.1:
        print(i)
        exit(0)