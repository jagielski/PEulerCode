def u(n):
    return 1-n+n*n-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
    
uli=[u(i) for i in range(1,18)]
gli=[i**3 for i in range(1,6)]

def lagr(li):
    def f(x):
        count = 0
        for i in range(len(li)):
            curval = li[i]
            for j in range(len(li)):
                if i!=j:
                    curval*=(x-j)/(i-j)
            count+=curval
        return count
    return f
    
ct=0
for i in range(10):
    print(lagr(uli[:i+1])(i+1),uli[i+1])
    if lagr(uli[:i+1])(i+1)!=uli[i+1]:
        ct+=lagr(uli[:i+1])(i+1)
print(ct)