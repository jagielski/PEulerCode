def sqrt(n):
    count = 0
    currdigits = n
    p = 0
    for i in range(100):
        x = 0
        while (x+1)*(20*p+x+1)<=currdigits:
            x+=1
        currdigits = 100*(currdigits-x*(20*p+x))
        p = p*10+x
        count += x
    if (count <= n):
        return 0
    else:
        return count
totalcount = 0
for i in range(100):
    totalcount += sqrt(i)
print(totalcount)