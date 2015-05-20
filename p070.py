primefile = open("primes1.txt")
primelist = []
currprimes = [int(val) for val in primefile.readline().split()]
while currprimes[0]<(10**7)//2:
    primefile.readline()
    for currprime in currprimes:
        primelist.append(currprime)
    currprimes = [int(val) for val in primefile.readline().split()]


def totient(n):
    if n<=1:
        return n
    currind = 0
    currprime = primelist[currind]
    currtot=n
    while currprime<n/2:
        if n%currprime==0:
            currtot*=(currprime-1)/currprime
        currind+=1
        currprime = primelist[currind]
    return int(currtot)

curmin = (0,100)
for i in range(2,10**7):
    if i%(10**5)==0:
        print(i)
    a = totient(i)
    if sorted(str(a))==sorted(str(i)):
        print(i,a)
        if i/a<curmin[1]:
            curmin = (i,i/a)
print(curmin)
        