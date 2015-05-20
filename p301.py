def factorial(k):
    fact = 1
    for i in range(1,k+1):
        fact*=i
    return fact
count = 0
for i in range(16):
    count+=(factorial(31-i)/(factorial(i)*factorial(31-2*i)))
print(count)