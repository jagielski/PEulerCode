def memoize(f):
    memo = {}
    def helper(x,y):
        if x not in memo:
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    return helper

@memoize
def ackermann(m,n):
    if m == 0:
        return (n+1)%(14**8)
    elif n == 0 and m>0:
        return ackermann(m-1,1)
    elif n>0 and m>0:
        return ackermann(m-1,ackermann(m,n-1))
print(ackermann(0,0)+ackermann(1,1)+ackermann(2,2)+ackermann(3,3)+ackermann(4,4))
