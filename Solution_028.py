# Write a Python program to find the second largest number in a list.

lst = [10, 50, 20, 30, 40, 50]

max_num = max(lst)

while True:
    if max_num in lst:
        lst.remove(max_num)
    else:
        break

print(f"The Second largest number is {max(lst)}")
