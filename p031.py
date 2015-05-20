coinvalues = [1,2,5,10,20,50,100,200]
sums = [{0:1},{0:1},{0:1},{0:1},{0:1},{0:1},{0:1}]
def combos(value, maxcoin):
    if value<0:
        return 0
    if maxcoin<=1 or value<=1:
        return 1
    currcoins = coinvalues[:maxcoin]
    print(value,currcoins)
    count = 0
    for i in range(len(currcoins)):
        count +=combos(value-currcoins[i],i+1)
    return count
print(combos(200,8))