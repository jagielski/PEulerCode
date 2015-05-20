def euclidean(a,b):
    if a*b==0:
        return a+b
    elif a<b:
        return euclidean(b,a)
    else:
        c = a%b
        return euclidean(b,c)

print(euclidean(4,1))
triplects = [0]*1001
n=1
while n*n<250:
    m = n+1
    while m*(m+n)<=500:
        print(m,n)
        if euclidean(m,n)==1 and (m-n)%2==1:
            perim = 2*m*n+2*m*m
            i = 1
            while perim*i<1000:
                triplects[perim*i]+=1
                i+=1
        m+=1
    n+=1
maxval = (1, triplects[1])
for i in range(1000):
    if triplects[i+1]>maxval[1]:
        maxval = (i+1, triplects[i+1])
print(maxval)