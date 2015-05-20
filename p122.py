from math import sqrt
f = open("primesunderthousand.txt")
primeli = []
for line in f:
    primeli.append(int(line.strip()))
primeli = primeli[:50]
    
def binct(n):
    ct = 0
    while n>0:
        if n%2==1:
            ct+=1
        n=n//2
        ct+=1
        
    return ct-2
    
        
def factorct(n):
    pass
    
bests = [0]*200
bests[0] = 0
for i in range(1,201):
    if i in primeli:
        bests[i-1]=binct(i)
    elif i%2==0:
        bests[i-1]=1+bests[i//2-1]
    else:
        for j in range(3,1+int(sqrt(i))):
            if i%j==0:
                print(j,bests[j-1])
                bests[i-1]=bests[j-1]+bests[(i//j)-1]
    print(i,bests[i-1])

print(sum(bests))
