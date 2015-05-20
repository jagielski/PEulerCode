alphanum = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

wordfile = open("p042_words.txt")
words = []
for word in wordfile.readline().split(','):
    words.append(word)
def value(word):
    count = 0
    for char in word.lower():
        if char in alphanum:
            count+=alphanum[char]
    return count

wordvals = []
for word in words:
    wordvals.append(value(word))
    
triangles = []
for i in range(21):
    triangles.append(i*(i+1)//2)    
    
count = 0    
for wordval in wordvals:
    if wordval in triangles:
        count+=1
        
print(count)