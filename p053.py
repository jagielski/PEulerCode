def factorial(k):
    fact = 1
    for i in range(1,k+1):
        fact*=i
    return fact
count = 0
for n in range(1,101):
    print(n)
    r = 0
    c = factorial(n)/(factorial(r)*factorial(n-r))
    while c<1000000 and r<n:
        r+=1
        c = factorial(n)/(factorial(r)*factorial(n-r))
    if r!=n:
        if n%2==1:
            count+=((1+n)//2-r)*2
        else:
            count += 1+2*(n//2-r)
    print(count)
print(count)