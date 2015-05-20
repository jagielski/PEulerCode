COMPLETE=[str(i) for i in range(1,10)]
pandset=set()
for cand in range(100,10000):
    for lier in range(1,1+10000//cand):
        if (sorted(str(cand)+str(lier)+str(cand*lier))==COMPLETE):
            print(cand,lier,cand*lier)
            pandset.add(cand*lier)
count = 0
for i in pandset:
    count+=i
print(count)