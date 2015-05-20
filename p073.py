from numthy import gcd
count = 0
for i in range(1,9):
    if i%1000==0:
        print(i)
    for j in range((i+2)//3,(i+1)//2):
        if gcd(i,j)==1:
            print(i,j)
            count+=1
print(count)