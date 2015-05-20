from sys import argv
a=int(argv[1])
b=int(argv[2])
def euclidean(a,b):
    if a*b==0:
        return a+b
    elif a<b:
        return euclidean(b,a)
    else:
        c = a%b
        return euclidean(b,c)  
print(euclidean(a,b))