def sumofdigits(n):
    count = 0
    while n>0:
        count+=n%10
        n = n//10
    return count

maxsum = 0
for a in range(100):
    for b in range(100):
        c = sumofdigits(a**b)
        if c>maxsum:
            maxsum = c
print(maxsum)