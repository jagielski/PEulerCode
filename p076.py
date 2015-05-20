parts = [0,1,2]
parts.extend([0]*99)
def partitions(value):
    if value<=0:
        return 0
    if parts[value]!=0:
        return parts[value]
    else:
        j=1
        while j*(3*j-1)/2<value:
            parts[value] += partitions(value-(3*j*j-j)//2)*(-1)**j
            j+=1
        return parts[value]
print(partitions(3))