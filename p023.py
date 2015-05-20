import math
abundants = []
def isabundant(n):
    divisorli = []
    for j in range(int(math.sqrt(n))):
        if n%(j+1)==0:
            divisorli.append(j+1)
    newdivs = []
    for div in divisorli:
        newdivs.append(int(n/div))
    divisorli.extend(newdivs)
    if math.sqrt(n)%1==0:
        divsum = sum(divisorli)-n-int(math.sqrt(n))
    else:
        divsum = sum(divisorli)-n
    return divsum>n
for i in range(28124):
    if isabundant(i):
        abundants.append(i)
abundantsum = set()
for ab1 in abundants:
    print(ab1)
    j=0
    while abundants[j]+ab1<=28123:
        abundantsum.add(ab1+abundants[j])
        j+=1
print(abundantsum)

nosumsum = 0
for i in range(28124):
    if not i in abundantsum:
        nosumsum+=i
print(nosumsum)