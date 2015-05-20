romanfile = open("p089_roman.txt")
romanlist = []
badcount = 0
for line in romanfile:
    romanlist.append(line.strip())
    badcount+=len(line.strip())
    
halves = ["V", "L", "D"]
tens = ["I", "X", "C", "M"]
valuedict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
def minimize(roman):
    for i in range(len(roman)):
        for j in range(len(halves)):
            if roman[i:].startswith(2*halves[j]):
                return minimize(roman[0:i]+tens[j+1]+roman[i+2:])
            elif roman[i:].startswith(5*tens[j]):
                return minimize(roman[0:i]+halves[j]+roman[i+5:])
            elif roman[i:].startswith(4*tens[j]):
                return minimize(roman[0:i+1]+halves[j]+roman[i+4:])
            elif len(roman)>i+2 and roman[i]+roman[i+2]==2*halves[j]:
                return minimize(roman[0:i]+roman[i+1]+tens[j+1]+roman[i+3:])
    return roman
    
goodcount = 0
for romanword in romanlist:
    newroman = minimize(romanword)
    print(minimize(romanword))
    goodcount+=len(newroman)
print(goodcount,badcount,badcount-goodcount)