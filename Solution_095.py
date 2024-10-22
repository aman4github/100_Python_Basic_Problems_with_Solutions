# Write a Python program to find the length of the longest word in a string.

str = input("Enter your String : ")
lst = []
lst2 = []
max_len = 0

lst.append(str.split())

for i in lst:
    for j in i:
        if len(j) > max_len:
            lst2.clear()
            max_len = len(j)
            lst2.append(j)
        elif max_len == len(j):
            if j not in lst2:
                lst2.append(j)
        
print(f"The longest word is {lst2} and the length is {max_len}")
