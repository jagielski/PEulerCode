from math import sqrt
from decimal import *
getcontext().prec = 40
class Surd:
    def __init__(self,a,b,d):
        self.a=a
        self.b=b
        self.d=d
        
    def __add__(self,other):
        assert (self.d==other.d)
        return Surd(self.a+other.a,self.b+other.b,self.d)
        
    def __sub__(self,other):
        assert (self.d==other.d)
        return Surd(self.a-other.a,self.b-other.b,self.d)

    def __mul__(self,other):
        assert (self.d==other.d)
        return Surd(self.a*other.a+self.d*other.b*self.b,self.b*other.a+self.a*other.b,self.d)
        
    def __div__(self,other):
        val = self.a*self.a-self.b*self.b*self.d
        return Surd(self.a/val,-self.b/val,self.d)*other
        
    def __eq__(self,other):
        return (self.a==other.a) and (self.b==other.b) and (self.d==other.d)
        
    def eval(self):
        return self.a+self.b*sqrt(self.d)
        
        
def contfrac(n):
    a=Surd(0,1,d)
    first=a-Surd(int(a.eval),0,d)
    
def contfrac(n):
    x = Decimal(n).sqrt()
    first = Decimal(x-int(x))
    if first==0:
        return 0
    period =0
    cur=0
    while cur!=first:
        cur = Decimal(1/(first))
        cur = Decimal(cur-int(cur))
        period +=1
    return period
    
for i in range(2,100):
    
"""count=0
for n in [Decimal(k) for k in range(1,10000)]:
    if n.sqrt()!=int(n.sqrt()):
        if contfrac(n)%2==1:
            count+=1
print(count)"""