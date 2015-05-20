primelist = [2,3,5,7,11,13,17]

mults17 = {}
i=0
while 17*i<1000:
    n = str(17*i)
    if len(set("0"*(3-len(n))+n)) == 3: # string length 3 padded with 0s contains no duplicates
        mults17[("0"*(3-len(n))+n)[0:2]] = n
    i+=1
print(mults17)

mults13 = {}
i=0
while 13*i<1000:
    n = str(13*i)
    if len(set("0"*(3-len(n))+n)) == 3: # string length 3 padded with 0s contains no duplicates
        mults13[("0"*(3-len(n))+n)[0:2]] = n
    i+=1
print(mults13)

mults11 = {}
i=0
while 11*i<1000:
    n = str(11*i)
    if len(set("0"*(3-len(n))+n)) == 3: # string length 3 padded with 0s contains no duplicates
        mults11[("0"*(3-len(n))+n)[0:2]] = n
    i+=1
print(mults11)

mults7 = {}
i=0
while 7*i<1000:
    n = str(7*i)
    if len(set("0"*(3-len(n))+n)) == 3: # string length 3 padded with 0s contains no duplicates
        k = ("0"*(3-len(n))+n)
        if k[0:2] in mults7:
            mults7[k[0:2]].append(k)
        else:
            mults7[k[0:2]] = [k]
    i+=1
print(mults7)

mults5 = {}
i=0
while 5*i<1000:
    n = str(5*i)
    if len(set("0"*(3-len(n))+n)) == 3: # string length 3 padded with 0s contains no duplicates
        k = ("0"*(3-len(n))+n)
        if k[0:2] in mults5:
            mults5[k[0:2]].append(k)
        else:
            mults5[k[0:2]] = [k]
    i+=1
print(mults5)

mults3 = {}
i=0
while 3*i<1000:
    n = str(3*i)
    if len(set("0"*(3-len(n))+n)) == 3: # string length 3 padded with 0s contains no duplicates
        k = ("0"*(3-len(n))+n)
        if k[0:2] in mults3:
            mults3[k[0:2]].append(k)
        else:
            mults3[k[0:2]] = [k]
    i+=1
print(mults3)

mults2 = []
i=50
while 2*i<1000:
    n = str(2*i)
    if len(set(n)) == 3: # string length 3 padded with 0s contains no duplicates
        mults2.append(n)
    i+=1
print(mults2)

count = 0
fullstr = "1234567890"
for mult2 in mults2:
    if mult2[1:] in mults3:
        for mult3 in mults3[mult2[1:]]:
            if mult3[1:] in mults5:
                for mult5 in mults5[mult3[1:]]:
                    if mult5[1:] in mults7:
                        for mult7 in mults7[mult5[1:]]:
                            if mult7[1:] in mults11:
                                mult11 = mults11[mult7[1:]]
                                if mult11[1:] in mults13:
                                    mult13 = mults13[mult11[1:]]
                                    if mult13[1:] in mults17:
                                        mult17 = mults17[mult13[1:]]
                                        print(mult2,mult3,mult5,mult7,mult11,mult13,mult17)
                                        mult9str = mult2+mult3[2]+mult5[2]+mult7[2]+mult11[2]+mult13[2]+mult17[2]
                                        if len(set(mult9str)) == len(mult9str):
                                            for elem in (set(fullstr)-set(mult9str)):
                                                print(elem+ mult9str)
                                                count+=int(elem+mult9str)

print(count)