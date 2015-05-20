for i in range(100000,166666):
    comp = sorted(str(i))
    if sorted(str(2*i))==comp and sorted(str(3*i))==comp and sorted(str(4*i))==comp and sorted(str(5*i))==comp and sorted(str(6*i))==comp:
        print(i)
        exit(0)