for i in range(1000000000,1500000000,100):
    if (i-1000000000)%10000000==0:
        print(i)
    for last2 in [30,70]:
        x = i+last2
        value = str(x*x)
        isit = True
        for j in range(1,9):
            if str(j)!=value[2*j-2]:
                isit = False
        if isit:
            print(x)
            exit(0)