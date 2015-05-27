# takes about half an hour - can be optimized, but it works!

from math import sqrt
from numthy import crt
from itertools import product

f = open("primes10000k.txt")
primeli = []
for line in f:
    primeli.append(int(line.strip()))

    
def isprime(p):
    min=0
    max=len(primeli)-1
    while min<=max:
        mid = (max+min)//2
        if primeli[mid]==p:
            return True
        elif primeli[mid]<p:
            min=mid+1
        else:
            max=mid-1
    return False
                
def factorize(n):
    if isprime(n):
        return {n:1}
    curind=0
    curprime=primeli[curind]
    while curprime<=sqrt(n):
        if n%curprime==0:
            pow=1
            n=n//curprime
            while n%curprime==0:
                n=n//curprime
                pow+=1
            d={curprime: pow}
            k=factorizations[n]
            for key in k:
                d[key]=k[key]
            return d
        curind+=1
        curprime=primeli[curind]
        
        
N=10**7

factorizations=[{},{}]
for i in range(2,N+1):
    if i%1000==0:
        print("factorizing:", i)
    factorizations.append(factorize(i))
    
# for i in range(len(factorizations)):
    # print(i,factorizations[i])


def M(n):
    f=factorizations[n]
    if len(f)==1:
        return 1
    mli=[]
    for k in f:
        mli.append(k**f[k])
    maxval=1
    for ali in product(range(2),repeat=len(mli)):    
        b=crt(ali,mli)%n
        if b>maxval:
            maxval=b
    return maxval
    
count=0
for i in range(2,N+1):
    m=M(i)
    if i%1000==0:
        print("CRTing:",i,m)
    count+=m
print(count)