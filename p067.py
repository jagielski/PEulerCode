trianglefile = open("p067_triangle.txt")
triangle=[]
for line in trianglefile:
    triangle.append([int(i) for i in line.strip().split()])
triangledistances = [triangle[i][:] for i in range(len(triangle))]
for i in range(1,len(triangledistances)):
    triangledistances[i][0]=triangledistances[i-1][0]+triangle[i][0]
    triangledistances[i][i]=triangledistances[i-1][i-1]+triangle[i][i]
for i in range(2,len(triangledistances)):
    for j in range(1,i):
        triangledistances[i][j] = triangle[i][j]+max(triangledistances[i-1][j],triangledistances[i-1][j-1])
maxdist = triangledistances[-1][0]        
for elem in triangledistances[-1]:
    if elem>maxdist:
        maxdist = elem
        
print(maxdist)