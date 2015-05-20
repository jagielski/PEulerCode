from math import log
powerfile = open("p099_base_exp.txt")
powerlist = []
for line in powerfile:
    powerlist.append([int(val) for val in line.strip().split(',')])

curmax = 0
for i in range(len(powerlist)):
    bepair = powerlist[i]
    if powerlist[curmax][1]*log(powerlist[curmax][0])<bepair[1]*log(bepair[0]):
        print(i, bepair)
        curmax = i
print(i)