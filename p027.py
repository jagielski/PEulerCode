from math import sqrt

primefile = open("primesunderthousand.txt")
primelist = []
for line in primefile:
    primelist.append(int(line.strip()))

def isPrime(number):
    if number < 2:
        return False
    i = 0
    curprime = 2
    root = sqrt(number)
    while curprime <= root:
        if number%curprime == 0:
            return False
        i+=1
        curprime = primelist[i]
    return True

curab = (1,41)
curmax = 39

for a in range(-1000,1001):
    print(a)
    for b in range(-1000,1001):
        c=0
        while isPrime(c*c + a*c + b):
            c+=1
        if c>curmax:
            curab = (a,b)
            print(a,b,curmax)
            curmax = c
print(curab, curmax, curab[0]*curab[1])