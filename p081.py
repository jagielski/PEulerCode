LENGTH = 80
matrixfile = open("p081_matrix.txt")
matrixvalues = [['']]*LENGTH
for i in range(LENGTH):
    matrixvalues[i]=[int(val) for val in matrixfile.readline().strip().split(',')]
print(matrixvalues)
distances = [[]]
distances = [matrixvalues[i][:] for i in range(LENGTH)]
for i in range(LENGTH):
    for j in range(LENGTH):
        distances[i][j]=0
distances[0][0]=matrixvalues[0][0]
for i in range(1,LENGTH):
    distances[i][0]=distances[i-1][0]+matrixvalues[i][0]
    distances[0][i]=distances[0][i-1]+matrixvalues[0][i]
print(distances)
for dist in range(2,LENGTH+1):
    for i in range(1,dist):
        distances[i][dist-i]=min(distances[i][dist-i-1],distances[i-1][dist-i])+matrixvalues[i][dist-i]
for dist in range(LENGTH-2,0,-1):
    for i in range(dist):
        distances[LENGTH-dist+i][LENGTH-(i+1)]=min(distances[LENGTH-dist+i-1][LENGTH-(i+1)],distances[LENGTH-dist+i][LENGTH-(i+1)-1])+matrixvalues[LENGTH-dist+i][LENGTH-(i+1)]
print(distances)
print(distances[LENGTH-1][LENGTH-1])