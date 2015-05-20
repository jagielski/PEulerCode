def M(n):
    last=1
    for i in range(2,n):
        if i*(i-1)%n==0:
            return n+1-i
    return last
for i in range(1,10):
    print(i,M(10**i))