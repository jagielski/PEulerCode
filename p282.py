def memoize2(f):
    memo = {}
    def helper(x,y):
        if (x,y) not in memo:
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    return helper
    
def memoize3(f):
    memo = {}
    def helper(x,y,z):
        if (x,y,z) not in memo:
            memo[(x,y,z)] = f(x,y,z)
        return memo[(x,y,z)]
    return helper
    
def memoize4(f):
    memo = {}
    def helper(x,y,z,w):
        if (x,y,z,w) not in memo:
            memo[(x,y,z,w)] = f(x,y,z,w)
        return memo[(x,y,z,w)]
    return helper
    
k=14**8
totk=(k*3)//(7)

@memoize3
def powmod(base, exp, mod):
    print("starting exponentiation")
    curpow=1
    b=base%mod
    c=exp
    while c>0:
        if c%2==1:
            curpow=curpow*b%mod
        c=c//2
        b=b*b%mod
    return curpow
   
@memoize4
def powtowmod(base, length, mod, totmod):
    print("starting tower:", length)
    curtow=1
    b=base
    c=length
    while c>0:
        if c%1000000==0:
            print("progress:", c)
        curtow=powmod(base,curtow,totmod)
        c-=1
    return curtow

@memoize2
def ackermann(m,n):
    if m == 0:
        return (n+1)%(k)
    elif m==1:
        return (n+2)%(k)
    elif m==2:
        return (2*n+3)%(k)
    elif m==3:
        return powmod(2,(n+3),k)-3
    elif m==4:
        return powtowmod(2,n+3,k, totk)
    elif m==5:
        if n==0:
            return ackermann(4,1)
        return ackermann(4,ackermann(5,n-1))
    elif m==6:
        if n==0:
            return ackermann(5,1)
        return ackermann(5,ackermann(6,n-1))
        
ack1=[]
for a in range(6):
    ack1.append(ackermann(a,a))

ack2=[]
for b in range(7):
    ack2.append(ackermann(6,b))

    
count = 0
count+=sum(ack1)%k
count=(count+ack2[6])%k
print(count)
