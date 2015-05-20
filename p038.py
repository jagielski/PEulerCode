total = "123456789"

for i in range(9000,10000):
    if list(total)==sorted(str(i)+str(2*i)):
        print(str(i)+str(2*i))