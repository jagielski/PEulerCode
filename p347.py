from math import sqrt,log
primefile = open("primes1.txt")
primelist = []
currprimes = [int(val) for val in primefile.readline().split()]
while currprimes[0]<5000000:
    for currprime in currprimes:
        primelist.append(currprime)
    primefile.readline()
    currprimes = [int(val) for val in primefile.readline().split()]


MAX = 10000000
def M(p,q):
    k = p*q
    maxp = int(log(MAX/(k))/log(p))
    curmax = k*p**maxp
    curval = curmax
    nexttry = 0
    while curval//p%p==0:
        nexttry = (curval*q)//p
        if nexttry>MAX:
            nexttry = nexttry//q
        if nexttry>curmax:
            curmax = nexttry
        curval = nexttry
    return curmax

count = 0
curind = 0
curprime = primelist[curind]
while curprime<sqrt(MAX):
    print(curprime)
    nextind = curind+1
    nextprime = primelist[nextind]
    while curprime*nextprime<MAX:
        a = M(curprime,nextprime)
        count+=a
        nextind+=1
        nextprime = primelist[nextind]
    curind+=1
    curprime = primelist[curind]
print(count)