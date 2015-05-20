def conv(num):
    wayoldnumer, wayolddenom = 0,0
    oldnumer, olddenom = 1,0
    numer,denom = 2,1
    for i in range(num):
        wayoldnumer=oldnumer
        wayolddenom=olddenom
        oldnumer=numer
        olddenom = denom
        if i%3 == 1:
            numer = 2*oldnumer*int((i+2)/3)+wayoldnumer
            denom = 2*olddenom*int((i+2)/3)+wayolddenom
        else:
            numer = oldnumer+wayoldnumer
            denom = olddenom+wayolddenom
    return (numer,denom)
    
def sod(number):
    cursum = 0
    while number>0:
        cursum += number%10
        number = number//10
    return cursum

print(sod(conv(99)[0]))