def repr(a,b):
    result = ''
    while a*a+b*b>0:
        while (a*a+b*b)%2==0:
            result = '0'+result
            (a,b)=(int((b-a)/2),int((-a-b)/2))
        a-=1
        result = '1'+result
        (a,b)=(int((b-a)/2),int((-a-b)/2))
    # print(result)
    count = 0
    for char in result:
        if char=='1':
            count += 1
    return count
    
# first = [-11,11]
# second = [-11,11]
# count = 0
# for i in first:
    # for j in second:
        # print(i,j,repr(i,j))
        # count +=repr(i,j)
        
# for i in second:
    # for j in first:
        # print(i,j,repr(i,j))
        # count +=repr(i,j)

# print(count)

(a,b)=(3,8)
count=0
con = [-1,1]
for k in con:
    print(a,b,repr(a,k*b))
    count+=repr(a,k*b)