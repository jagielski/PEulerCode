from math import log10
def ispalindrome(number):
    length = log10(number)//1
    first = number // (10**length)
    last = number % 10
    if (first != last):
        return False
    else:
        newnum = (number-first*10**length)//10
        if (newnum < 10):
            return True
        else:
            return ispalindrome((number-first*10**length)//10)

def reverse(number):
    newnum = 0
    while (number >0):
        newnum *= 10
        digit = number % 10
        newnum += digit
        number = number // 10
    return newnum
    
notlychrels = set()
lychrels = set()
    
def islychrel(number):
    global notlychrels, lychrels
    newnum = set()
    curr = number
    newnum.add(curr)
    for i in range(50):
        curr += reverse(curr)
        newnum.add(curr)
        if ispalindrome(curr) or (curr in notlychrels):
            notlychrels = notlychrels.union(newnum)
            return False
        if (curr in lychrels):
            lychrels = lychrels.union(newnum)
            return True
    lychrels = lychrels.union(newnum)
    return True
    
count = 0
for value in range(10000):
    curr = 10000 - value
    if islychrel(curr):
        print(curr)
        count += 1
print("Count:", count)