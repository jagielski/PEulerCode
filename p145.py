def reverse(n):
    result = 0
    while n>0:
        result=10*result+n%10
        n = n//10
    return result

def isodd(n):
    while n>0:
        if n%2 == 0:
            return False
        n=n//10
    return True
print(isodd(121212+reverse(121212)))
for exp in range(0,9):
    oddcount = 0
    print(10**(exp))
    if exp == 8:
        for i in range(10**(exp),10**(exp+1)):
            if i%10 !=0 and isodd(i+reverse(i)):
                oddcount+=1
    print(oddcount)

# for exp in range(0,8):
    # for i in range(10**exp,6*10**exp):
        # if i%10 !=0 and isodd(i+reverse(i)):
            # oddcount+=2
