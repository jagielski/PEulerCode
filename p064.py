from math import sqrt
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
    first=a-Surd(int(a.eval))