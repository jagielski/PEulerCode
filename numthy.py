def solvelincong(a,b,n):
    """solves ax=b mod n, finding the minimum positive solution"""
    a=a%n
    b=b%n
    # uses extgcd to find coefficients p,q for pa+qn=1
    inv = extgcd(a,n)
    return (inv[0]*b)%n
    
def gcd(a,b):
    if a*b==0:
        return a+b
    elif a<b:
        return gcd(b,a)
    else:
        c = a%b
        return gcd(b,c)  

def extgcd(a,b):
    """Extended Euclidean algorithm, pseudocode from wikipedia"""
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r%r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)       
    return (old_s, old_t, old_r)

def jacobi(a,n):
    val=1
    top=a%n
    bottom=n
    while top%2==0:
        top=top//2
        if ((bottom*bottom-1)//8)%2!=0:
            val=-val
    while top!=1:
        top, bottom = bottom, top
        if bottom%4==3 and top%4==3:
            val=-val
        top=top%bottom
        # print(top,bottom)
        if extgcd(top,bottom)[2]!=1:
            return 0
        while top%2==0:
            
            top=top//2
            if ((bottom*bottom-1)//8)%2!=0:
                val=-val
    return val

                
def perfectpower(n):
    """Checks to see if n is a perfect power - uses built in sieve of eratosthenes (code from stackoverflow) to only check prime roots"""
    from math import log2
    maxexp = int(log2(n))+1
    a = [True] * maxexp                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            if n**(1/i)==int(n**(1/i)):
                return True
            for n in range(i*i, maxexp, i):     # Mark factors non-prime
                a[n] = False
    return False

def aks(n):
    if perfectpower(n):
        return False
    minorder = int(log2(n)**2)
    
def crt(ali,mli):
    # print(ali,mli)
    M=1
    for m in mli:
        M*=m
    bli=[]
    for i in range(len(ali)):
        bli.append(solvelincong(M//mli[i],1,mli[i]))
    result=sum([ali[i]*bli[i]*(M//mli[i]) for i in range(len(ali))])%M
    return result
    
def powmod(base,exp, mod):
    """calculates a\equiv base^exp \mod{mod}"""
    a=1
    b=base%mod
    c=exp
    while c>0:
        if c%2==1:
            a=a*b%mod
        c=c//2
        b=b*b%mod
    return a
    
def solostrass(a,n):
    """False: composite; True: probably prime"""
    if gcd(a,n)!=1:
        return False
    elif powmod(a,(n-1)//2,n)!=(jacobi(a,n)+n)%n:
        return False
    else:
        return True
        
def millerrabin(a,n):
    """False: composite; True: probably prime"""
    if extgcd(a,n)[2]!=1:
        return False
    m=n-1
    s=0
    while m%2==0:
        m=m//2
        s+=1
    b=powmod(a,m,n)
    cur=b
    prev=1
    for exp in [2**k for k in range(1,s+1)]:
        prev=cur
        cur=(prev*prev)%n
        if cur==1 and (prev!=1 and prev!=n-1):
            return False
    if (cur%n)!=1:
        return False
    return True
        
def pollrhofactor(n):
    x=2
    y=2
    c=1
    while c==1:
        x=(x*x+1)%n
        y=(y**4+2*y*y+2)%n
        print(x,y)
        c=extgcd(y-x,n)[2]
    if c==n:
        return False
    return (c,n//c)
    

def pollrhodlog(p,g,h):
    def f(xab):
        (x,a,b)=xab[0],xab[1],xab[2]
        if x%3==0:
            return ((x**2)%p,(a+a)%(p-1),(b+b)%(p-1))
        if x%3==1:
            return ((x*g)%p,(a+1)%(p-1),b)
        if x%3==2:
            return ((x*h)%p,a,(b+1)%(p-1))
    x=f((1,0,0))
    y=f(f((1,0,0)))
    i=0
    while (x[0]!=y[0]):
        if i<3:
            print(x,y)
        x=f(x)
        y=f(f(y))
        i+=1
    print(g,'^',x[1],'*',h,'^',x[2],"=",g,'^',y[1],'*',h,'^',y[2],"in", i, "steps")
    
        
if __name__ == '__main__':
    #print(crt([2,3,1],[3,4,5]))
    #print(extgcd(1021763679,519424709))
    #print(powmod(1244183534,252426389,1889570071)*powmod(solvelincong(732959706,1,1889570071),496549570,1889570071)%1889570071)
    #print(powmod(1244183534,solvelincong(1021763679,1,1889458672),1889570071),powmod(732959706,solvelincong(519424709,1,1889458672),1889570071))
    #print(jacobi(1001,9907),jacobi(107,23),jacobi(1411,317),jacobi(1735,507))
    #for n in [294409,118901509,118901521]:
    #    for a in [2,3,5,17]:
    #        print(a,n,solostrass(a,n),millerrabin(a,n))    
    print(pollrhofactor(94134947))
    pollrhodlog(1299743,5,319806)
    print(powmod(5,362806,1299743)*powmod(319806,430782,1299743)%1299743 == powmod(5,772626,1299743)*powmod(319806,322080,1299743)%1299743)
    print(powmod(5,409820,1299743)==powmod(319806,108702,1299743))
    print(extgcd(108702,1299742))
    print(409820*124089%1299742)
    print(powmod(5,409820*124089,1299743)==powmod(319806,2,1299743),powmod(5,409820*124089,1299743)==powmod(5,448488,1299743))
    print(224244,powmod(5,224244,1299743)==319806,224244+1299743//2,powmod(5,224244+1299743//2,1299743)==319806)
    