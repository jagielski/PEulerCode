def memoize(f):
    memo = {}
    def helper(x,y):
        if (x,y) not in memo:            
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    return helper
            
@memoize
def p(t,b):
    if t<b:
        return 0
    if b==0:
        return 1
    return p(t-1,b-1)*(1/(t+1))+p(t-1,b)*((t)/(t+1))
    
print(1/p(15,8))
"""counttot=0
for i in range(15,7,-1):
    print(i)
    counttot+=p(15,i)
print(1/counttot)"""