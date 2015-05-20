from math import sqrt
#primes 4n+1
#52 - cube times square time single
primefile = open("primes1.txt")
primelist = []
i=0
for line in primefile:
    currprimes = [int(val) for val in line.strip().split()]
    for currprime in currprimes:
        if currprime%4==1:
            primelist.append(currprime)
    i+=1

def isprime(value):
    low = 0
    high = len(primelist)
    mid = (low + high) // 2
    while (low<=high):
        mid = (low + high) // 2
        midval = primelist[mid]
        if midval == value:
            return True
        elif midval < value:
            low = mid + 1
        else:
            high = mid - 1
    return False

def sumbefore(number):
    # one prime
    currind = 0
    primect = 0
    currprime = primelist[currind]
    while currprime<=number:
        newval = int(number//currprime)
        primect+=currprime*(newval*(newval+1)//2)
        currind+=1
        currprime = primelist[currind]
    
    # two primes
    doubleprimect = 0
    currind = 0
    currprime = primelist[currind]
    while currprime<=sqrt(number):
        currind1 = currind+1
        currprime1 = primelist[currind1]
        while currprime1*currprime <= number:
            newval = int(number//(currprime1*currprime))
            doubleprimect+=currprime*currprime1*(newval*(newval+1)//2)
            currind1+=1
            currprime1 = primelist[currind1]
        currind+=1 
        currprime = primelist[currind]
    
    # three primes
    tripleprimect = 0
    currind = 0
    currprime = primelist[currind]
    while currprime<=(number)**(1/3):
        currind1 = currind+1
        currprime1 = primelist[currind1]
        while currprime1*currprime <= number/17:
            currind2 = currind1+1
            currprime2 = primelist[currind2]
            while currprime2*currprime1*currprime <= number:
                newval = int(number//(currprime*currprime1*currprime2))
                tripleprimect+=currprime*currprime1*currprime2*(newval*(newval+1)//2)
                currind2+=1
                currprime2 = primelist[currind2]
            currind1+=1
            currprime1 = primelist[currind1]
        currind+=1 
        currprime = primelist[currind]
    
    # four primes??!!
    quadprimect = 0
    currind = 0
    currprime = primelist[currind]
    while currprime<=sqrt(sqrt(number)):
        currind1 = currind+1
        currprime1 = primelist[currind1]
        while currprime1*currprime <= sqrt(number):
            currind2 = currind1+1
            currprime2 = primelist[currind2]
            while currprime2*currprime1*currprime <= number/29:
                currind3 = currind2+1
                currprime3 = primelist[currind3]
                while currprime3*currprime2*currprime1*currprime <= number:
                    newval = int(number//(currprime*currprime1*currprime2*currprime3))
                    quadprimect+=currprime*currprime1*currprime2*currprime3*(newval*(newval+1)//2)
                    currind3 += 1
                    currprime3 = primelist[currind3]
                currind2+=1
                currprime2 = primelist[currind2]
            currind1+=1
            currprime1 = primelist[currind1]
        currind+=1 
        currprime = primelist[currind]
    
    # yeah, five primes shouldn't happen
    pentprimect = 0
    currind = 0
    currprime = primelist[currind]
    while currprime<=(number)**(0.2):
        currind1 = currind+1
        currprime1 = primelist[currind1]
        while currprime1*currprime <= (number)**(0.4):
            currind2 = currind1+1
            currprime2 = primelist[currind2]
            while currprime2*currprime1*currprime <= number**(0.6):
                currind3 = currind2+1
                currprime3 = primelist[currind3]
                while currprime3*currprime2*currprime1*currprime <= number**(0.8):
                    currind4 = currind3+1
                    currprime4 = primelist[currind4]
                    while currprime4*currprime3*currprime2*currprime1*currprime <= number:
                        newval = int(number//(currprime*currprime1*currprime2*currprime3*currprime4))
                        pentprimect+=currprime*currprime1*currprime2*currprime3*currprime4*(newval*(newval+1)//2)
                        currind4 += 1
                        currprime4 = primelist[currind4]
                    currind3 += 1
                    currprime3 = primelist[currind3]
                currind2+=1
                currprime2 = primelist[currind2]
            currind1+=1
            currprime1 = primelist[currind1]
        currind+=1 
        currprime = primelist[currind]
        
    integer = number//1
    result = (integer*(integer+1)//2)-primect+doubleprimect-tripleprimect+quadprimect-pentprimect
    return result
    
def quadreduce(N):
    count = 0
    for i in range(1,(N+1)//2):
        if ((N+sqrt(N*N+4*N*i-4*i*i))/2==(N+sqrt(N*N+4*N*i-4*i*i))//2):
            count +=1
            #print(i,(N+sqrt(N*N+4*N*i-4*i*i))/2)
    if count != 0:
        print(N, count)
        return count
for k in range(25*13*17-5,25*13*17+5):
    print(k,sumbefore(k))
    
"""
def count321():  
    count = 0
    firstindex = 0
    maxval = ((10**11)/(13*5**2))**(1/3)
    while primelist[firstindex] < 1.3*maxval:
        prime1 = primelist[firstindex]
        print(prime1)
        secondindex = 0
        maxval1 = sqrt((10**11)/(prime1**3*5))
        while primelist[secondindex] < 1.3*maxval1:
            if secondindex != firstindex:
                prime2 = primelist[secondindex]
                thirdindex = 0
                maxval2 = (10**11)/((prime1**3)*(prime2**2))
                while primelist[thirdindex] < 1.3*maxval2:
                    if (thirdindex != firstindex) and (thirdindex != secondindex):
                        prime3 = primelist[thirdindex]
                        value = prime3*(prime2**2)*(prime1**3)
                        multiplier = sumbefore(10**11/value)
                        count+=value*multiplier
                    thirdindex+=1
            secondindex+=1
        firstindex+=1
    return count

def count102():
    count = 0
    firstindex = 0
    prime1 = primelist[firstindex]
    print(prime1)
    secondindex = 0
    maxval1 = sqrt((10**11)/(prime1**10))
    while primelist[secondindex] < 1.3*maxval1:
        if secondindex != firstindex:   
            prime2 = primelist[secondindex]
            value = (prime1**10)*(prime2**2)
            multiplier = sumbefore(10**11/value)
            count += value*multiplier
        secondindex+=1
    return count
    
def count73():
    count = 0
    firstindex = 0
    maxval = ((10**11)/(5**3))**(1/7)
    while primelist[firstindex] < 1.3*maxval:
        prime1 = primelist[firstindex]
        print(prime1)
        secondindex = 0
        maxval1 = ((10**11)/(prime1**7))**(1/3)
        while primelist[secondindex] < 1.3*maxval1:
            if secondindex != firstindex:
                prime2 = primelist[secondindex]
                value = (prime1**7)*(prime2**3)
                multiplier = sumbefore(10**11/value)
                count += value*multiplier
            secondindex+=1
        firstindex+=1
    return count
    
def count64():
    count = 0
    firstindex = 0
    maxval = ((10**11)/(5**4))**(1/6)
    while primelist[firstindex] < 1.3*maxval:
        prime1 = primelist[firstindex]
        print(prime1)
        secondindex = 0
        maxval1 = sqrt(sqrt(10**11/(prime1**6)))
        while primelist[secondindex] < 1.3*maxval1:
            if secondindex!=firstindex:
                prime2 = primelist[secondindex]
                value = (prime1**6)*(prime2**4)
                multiplier = sumbefore(10**11/value)
                count += value*multiplier
            secondindex+=1
        firstindex+=1
    return count
totalcount = count321()+count102()+count73()#+count64()
print(str(totalcount))
while totalcount>0:
    print(totalcount%10)
    totalcount = totalcount // 10"""
# 274946541714329408