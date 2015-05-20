ak=2
currnum = 3
currdenom = 2
prevnum = 1
prevdenom = 1
count = 0
for i in range(1000):
    print(currnum,currdenom)
    a = prevdenom + 2*currdenom
    b = prevnum + 2*currnum
    prevnum = currnum
    prevdenom = currdenom
    currdenom = a
    currnum = b
    if len(str(currnum))>len(str(currdenom)):
        count += 1
print(count)