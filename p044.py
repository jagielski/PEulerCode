from math import sqrt
def isPent(num):
    quad = (1 + sqrt(1+24*num))/6
    return quad == int(quad)    

def pentlist(length):
    curlist = []
    for i in range(1,length):
        curlist.append(i*(3*i-1)/2)
    return curlist

LENGTH = 2500
pentsums = []
pentdiffs = []
allpents = pentlist(LENGTH)
for i in range(LENGTH-1):
    curpenti = allpents[i]
    for j in range(i):
        curpentj = allpents[j]
        if isPent(curpenti+curpentj):
            print(curpenti,curpentj,curpenti+curpentj)
            pentsums.append((curpenti,curpentj,curpenti+curpentj,curpenti-curpentj))
        if isPent(curpenti-curpentj):
            print(curpenti,curpentj,curpenti-curpentj)
            pentdiffs.append((curpenti,curpentj,curpenti+curpentj,curpenti-curpentj))
print(pentsums)
print(pentdiffs)
foundmatch = 0
for i in pentsums:
    for j in pentdiffs:
        if i[0] == j[0] and i[1] == j[1]:
            foundmatch += 1
            print(i,j)
            print(isPent(i[0]),isPent(i[1]),isPent(i[1]+i[0]),isPent(i[0]-i[1]))
            
print(foundmatch)