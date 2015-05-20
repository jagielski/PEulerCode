m = 4
def euclidean(a,b):
    if a*b==0:
        return a+b
    elif a<b:
        return euclidean(b,a)
    else:
        c = a%b
        return euclidean(b,c)  
#     a
#b       d
#  c
#
squares = set()
for i in range(1,142):
    squares.add(i*i)
count=0
for a in range(1,m+1):
    print(a)
    for b in range(1,m+1):
        for c in range(1,m+1):
            for d in range(1,m+1):
                if (a*b+b*c+c*d+d*a-(euclidean(a,b)+euclidean(b,c)+euclidean(c,d)+euclidean(d,a)))//2-1 in squares:
                    print(a,b,c,d,(a*b+b*c+c*d+d*a-(euclidean(a,b)+euclidean(d,c)+euclidean(c,d)+euclidean(d,a)))//2-1)
                    count+=1
print(count)