from sys import argv
f=open(argv[1])
dictfreq={}
for line in f:
    for char in line:
        if not char in dictfreq:    
            dictfreq[char]=0
        dictfreq[char]+=1
        
li=[]
for key in dictfreq:
    li.append((key,dictfreq[key]))
li=sorted(li,key=lambda elem: elem[1])
print(li)
