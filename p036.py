def isPalindrome(palin):
    if str(palin)==str(palin)[::-1]:
        return True
    return False

def toBinary(decimal):
    binstr = ''
    while decimal>0:
        lastdigit = decimal%2
        binstr+=str(lastdigit)
        decimal = decimal//2
    return binstr
    
cursum = 0
for i in range(1000000):
    if isPalindrome(i) and isPalindrome(toBinary(i)):
        print(i)
        cursum+=i
print(cursum)