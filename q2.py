Q1 = input("Enter the list of strings: ").split()
n = len(Q1)

class selection_sort:
    def Q2(self):
        for i in range(n-1):
            min_index = i
            for j in range (i+1,n):
                if Q1[j] < Q1[min_index]:
                    min_index = j

            Q1[i],Q1[min_index] = Q1[min_index],Q1[i]

selection_sort().Q2()
print(Q1)
