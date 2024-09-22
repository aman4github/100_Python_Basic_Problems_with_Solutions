# Write a Python program to count the frequency of elements in a list.

lst1 = [10, 50, 20, 30, 10, 40, 50]

# Method 1 

freq_num = 10

print(f"Frequency of number 10 = {lst1.count(freq_num)}")

# Method 2 

flag = 0

for i in lst1:
    if i == freq_num:
        flag += 1

if flag > 0:
    print(f"Frequency of number 10 = {lst1.count(freq_num)}")
else:
    print("Number does not exist in the list")

