n = int(input("Enter the number of points: "))
print("Enter the points: ")
i = 1
c = []
while i<=n:
    print("Enter point " + str(i))
    i+=1
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    c.append((x,y))
print("Enter the reference point: ")
xr = int(input("Enter the x coordinate: "))
yr = int(input("Enter the y coordinate: "))
ref = (xr,yr)
dist = []
for ch in c:
    d = (ch[0] - xr)**2 + (ch[1] - yr)**2
    dist.append(d)
n = len(dist)
for j in range(n):
    min = j
    for k in range(j+1,n):
        if dist[k]<dist[min]:
            min = k
    dist[j],dist[min] = dist[min],dist[j]
    c[j],c[min] = c[min],c[j]

print(c)


    
