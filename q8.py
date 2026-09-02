import csv
cone = []
dist = []

with open("cones.csv", "r") as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        
        if i == 0:
            i+=1
            continue

        else:
            x = int(row[1])
            y = int(row[2])
            d = x**2 + y**2
            dist.append(d)
            cone.append(row)
            i+=1
            
        
    n = len(dist)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if dist[j]<dist[min]:
                min = j
        dist[i],dist[min] = dist[min],dist[i]
        cone[i],cone[min] = cone[min],cone[i]


    b = []
    y = []
    for row in cone:
        if row[3] == "blue":
            b.append(row)
        else:
            y.append(row)

with open("blue.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for row in b:
        writer.writerow(row)


with open("yellow.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for row in y:
        writer.writerow(row)

centre = []

for blue in b:
    xb = int(blue[1])
    yb = int(blue[2])

    dis = []

    for yellow in y:
        xy = int(yellow[1])
        yy = int(yellow[2])

        d = (xb - xy)**2 + (yb - yy)**2
        dis.append(d)

    # Find index of smallest distance
    min_index = 0

    for i in range(1, len(dis)):
        if dis[i] < dis[min_index]:
            min_index = i

    # This is the yellow cone you want
    nearest_yellow = y[min_index]

    # Get its coordinates
    xy = int(nearest_yellow[1])
    yy = int(nearest_yellow[2])

    # Midpoint
    mx = (xb + xy) / 2
    my = (yb + yy) / 2

    centre.append((mx, my))

with open("centreline.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for row in centre:
        writer.writerow(row)





        

        
        

