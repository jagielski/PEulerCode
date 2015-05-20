count = 0
for power in range(70):
    for i in range(10):
        if len(str(i**power)) == power:
            print(power, i)
            count +=1
print(count)