# this one works takes a few minutes

# theory - a prime p is a hamming prime if p-1 is a hamming number
# phi(n)=n*product((p_i-1)/p_i) for all primes p_i which divide n
# then phi(n) is hamming iff n = h*k, where h is hamming and k is the product of distinct hamming primes

from math import sqrt
f = open("primes1000k.txt")
primeli = []
for line in f:
    primeli.append(int(line.strip()))

N=10**12

def hammings(N):
    curpower = 1
    twopowers = []
    while curpower<N:
        twopowers.append(curpower)
        curpower*=2
    curpower = 1
    threepowers = []
    while curpower<N:
        threepowers.append(curpower)
        curpower*=3
    curpower = 1
    fivepowers = []
    while curpower<N:
        fivepowers.append(curpower)
        curpower*=5
    hammingsli = []
    for twopower in twopowers:
        for threepower in threepowers:
            for fivepower in fivepowers:
                curhamming = twopower*threepower*fivepower
                if curhamming<=N:
                    hammingsli.append(curhamming)
                else:
                    break
    return(sorted(hammingsli))

def hammingprimes(N):
    hamprimes = []
    for i in hammingli:
        if naiveprimetest(i+1) and i+1>5: 
            print(i+1)
            hamprimes.append(i+1)
    return hamprimes
    
    
def naiveprimetest(n):
    curprime = primeli[0]
    curind = 0
    while curprime<=sqrt(n):
        if n%curprime==0:
            return False
        curind+=1
        curprime = primeli[curind]
    return True
    
hammingli = hammings(N)
hamprimeli = hammingprimes(N)
hammingsums = [hammingli[0]]
for i in range(1,len(hammingli)):
    hammingsums.append((hammingsums[i-1]+hammingli[i])%(2**32))
#print(hammingli)
    
def sumunder(n):
    if n==0:
        return 0
    curind=0
    curham=hammingli[curind]
    while curham<=n and curind<len(hammingli)-1:
        curind+=1
        curham=hammingli[curind]
    if curind==len(hammingli)-1:
        return hammingsums[-1]
    return hammingsums[curind-1]
    
print(sumunder(15))
print(sumunder(100))
print(sum(hammingli)%2**32,2**32+(hammingsums[-1]-10**12)%2**32,sumunder(10**12-1),sumunder(10**12-1)+10**12%2**32)


def counthamtots(M,maxind):
    """we make a max prime index in order to ensure only one of each prime is counted and each prime combination
    is only counted once"""
    if M==0 or M==1:
        return M
    count = sumunder(M)
    for ind in range(maxind):
        if M==10**12:
            print(hamprimeli[ind],maxind,count)
        count=(count+hamprimeli[ind]*counthamtots(M//hamprimeli[ind],ind))%(2**32)
    return count%(2**32)
    
print(counthamtots(N,len(hamprimeli)))