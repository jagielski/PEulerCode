def rng(n):
    i=0
    x = 290797
    while i<n:
        x=x*x%50515093
        i+=1
    return x
    
def nf(p,q):
    
list = [rng(i) for i in range(10)]

print(list)