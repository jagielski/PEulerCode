primefile=open("primes10000k.txt")
primeli=[]
for line in primefile:
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
for i in range(0,10):
    x=i*1110+1
    print(x,isprime(x))
for prime in primeli:
    a = list(str(prime))
    count=0
    if a.count('0')==3:
        for i in range(1,10):
            m=int(''.join([x if x!='0' else str(i) for x in a]))
            if isprime(m):
                count+=1
    if count==7:
        print(prime)
        exit(0)
    count=0
    if a.count('1')==3:
        for i in range(2,10):
            if isprime(int(''.join([x if x!='1' else str(i) for x in a]))):
                count+=1
    if count==7:
        print(prime)
        exit(0)
    count=0
    if a.count('2')==3:
        for i in range(3,10):
            if isprime(int(''.join([x if x!='2' else str(i) for x in a]))):
                count+=1
    if count==7:
        print(prime)
        exit(0)
        
        