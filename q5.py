n = int(input("Enter the number of integers: "))
i = 1
a = []
while i<=n:
    num = int(input("Enter integer " + str(i) + ":"))
    a.append(num)
    i+=1

ht = [[] for i in range(10)]

for i in a:
    j = i % 10
    ht[j].append(i)
            

print(ht)


    
