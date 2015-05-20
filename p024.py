def factorial(num):
    curfac = 1
    for i in range(num):
        curfac *= i+1
    return curfac

def lexperm(num, length):
    num-=1
    valuelist = list(range(length))
    curperm = ''
    while len(valuelist)>0:
        remain = num%factorial(length-1)
        index = num//factorial(length-1)
        print(num, remain, index, valuelist)
        curperm += str(valuelist[index])
        valuelist.remove(valuelist[index])
        num = remain
        length-=1
    return curperm
    
print(lexperm(1000000,10))