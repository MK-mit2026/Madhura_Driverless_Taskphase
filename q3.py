
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

class binary_search:
    def f(self):
        low = 0
        high = len(Q1) - 1

        while low <= high:
            mid = (high + low)//2
            if Q1[mid] == s:
                print("String found at index: " + str(mid))
                break
            elif Q1[mid] > s:
                high = mid - 1
            elif Q1[mid] < s:
                low = mid + 1
            else:
                print("String not found")
                break

#from Task2 import Q1, selection_sort



s = input("Enter the string to be searched for: ")

binary_search().f()