"""
p190.py - lagrange multipliers to the rescue! 1/x_1=2/x_2=3/x_3=...
"""

count=0
mult=0
for i in range(2,16):
    x1=2/(i+1)
    powers=x1
    for j in range(2,i+1):
        powers*=(x1*j)**j
    print(i,int(powers))
    count+=int(powers)
print(count)