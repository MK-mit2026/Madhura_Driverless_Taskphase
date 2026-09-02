n = int(input("Enter an integer n: "))
print("Enter " + str(n) + " strings: ")
i = 1
strings = []
while i<=n:
    s = input("Enter string " + str(i) + ": ")
    strings.append(s)
    i += 1

dictionary  = {}

for s in strings:
    for ch in s.lower():
        if ch.isalpha():
            if ch in dictionary:
                dictionary[ch] += 1
            else:
                dictionary[ch] = 1
            
print(dictionary)
