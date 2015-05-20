def ds(num):
    cursum = 0
    while num>0:
        cursum+=(num%10)**2
        num=num//10
    return cursum
    
def chain(num):
    curval = num
    while not (curval in set89s or curval in set1s):
        curval = ds(curval)
    if curval in set89s:
        set89s.add(num)
        return True
    else:
        set1s.add(num)
        return False
        
set89s = {89}
set1s = {1}

curcount = 0
for i in range(1,10000000):
    if chain(i):
        curcount+=1
    if i%100000 == 0:
        print(i)
print(curcount)