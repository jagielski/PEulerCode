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
    
    

if __name__ == '__main__':
    print(perfectpower(5**101))