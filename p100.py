# (b/n)*(b-1/n-1)=1/2 - n^2-n=2b^2-2b
# (b/(b+r))*((b-1)/(b+r-1))=1/2 - 2br+r^2-r=b^2-b
# given n, n=(1+sqrt(1+4(2b^2-2b)))/2
from decimal import *
getcontext().prec = 30
from math import sqrt

n=1070379110497
print(n//10**12)
val = Decimal(2*n*n-2*n+1).sqrt()
if int(val)-val==0:
    print(n, (val+1)//2)
