"""
p146.py - use chinese remainder theorem a few times to get a couple congruence classes mod 2730, then do exactly what the problem asks for
"""
from numthy import millerrabin


def detmilrab(n):
    for a in [2,3,5,7,11,13,17,19,23]:
        if not millerrabin(a,n):
            return False
    return True
        
square=0
count=0
for a in range(150000000):
    if a%1000000==0:
        print(a)
    if a%2730 in [430,640,2110,1270,10,220,1340,1550,290,2180,920,1130,1600,1810,550,2440,1180,1390,2510,2720,1460,620,2090,2300]:
        square=a*a
        if detmilrab(square+1) and detmilrab(square+3) and detmilrab(square+7) and detmilrab(square+9) and detmilrab(square+13) and detmilrab(square+27) and not(detmilrab(square+21)):
            count+=a
            print("valid",a)
print(count)