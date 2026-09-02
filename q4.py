n1 = int(input("Enter the number of rows of first matrix: "))
m1 = int(input("Enter the number of columns of first matrix: "))

n2 = int(input("Enter the number of rows of second matrix: "))
m2 = int(input("Enter the number of columns of second matrix: "))

if m1 == n2:
    print("Enter the first matrix: ")

    a = []
    i = 1

    while i <= n1:
        row1 = []
        j = 1

        while j <= m1:
            c = int(input("Enter the element in row " + str(i) + " and column " + str(j) + ": "))
            row1.append(c)
            j += 1

        a.append(row1)
        i += 1
    print("Enter the second matrix: ")
    b = []
    l = 1
    
    while l <= n2:
        row2 = []
        k = 1
    
        while k <= m2:
            d = int(input("Enter the element in row " + str(l) + " and column " + str(k) + ": "))
            row2.append(d)
            k += 1
    
        b.append(row2)
        l += 1

    result = []
    i = 0

    while i < n1:

        result_row = []

        j = 0

        while j < m2:

            total = 0

            k = 0

            while k < m1:


                total = total + a[i][k] * b[k][j]

                k += 1

            result_row.append(total)
            j += 1

        result.append(result_row)
        i += 1

    print("The resultant matrix is: ")
    print(result)
                
   
else:
    print("The matrices cannot be multiplied")





