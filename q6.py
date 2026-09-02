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

    low = 0
    high = len(ht[j]) - 1

    while low <= high:

        mid = (low + high) // 2

        if ht[j][mid] < i:
            low = mid + 1

        else:
            high = mid - 1

    ht[j].insert(low,i)

print(ht)   
        
        




            

print(ht)