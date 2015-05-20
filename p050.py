from math import sqrt
f = open("primesunderthousand.txt")
primelist = []
for line in f:
    primelist.append(int(line.strip()))

def isPrime(num):
    i = 0
    curprime = 2
    while curprime <= sqrt(num):
        if num%curprime == 0:
            return False
        i+=1
        curprime = primelist[i]
    return True
    
maxcount = 0
maxprime = 0
for i in range(len(primelist)):
    curnum = 0
    curcount = 0
    while curnum<1000000 and i<len(primelist):
        curnum += primelist[i]
        curcount +=1
        print(curnum)
        if isPrime(curnum) and curcount>maxcount:
            maxprime = curnum
            maxcount = curcount
            print(maxcount,maxprime)
        i+=1
print(maxcount, maxprime)