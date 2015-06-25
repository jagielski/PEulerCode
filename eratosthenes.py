def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
                
primefile = open("primes2108.txt","w")
for prime in primes_sieve(2*10**8):
    primefile.write(str(prime)+'\n')
