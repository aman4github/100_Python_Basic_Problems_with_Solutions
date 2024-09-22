# Write a Python program to find the second smallest number in a list.

lst = [10, 50, 20, 30, 10, 40, 50]

min_num = min(lst)

while True:
    if min_num in lst:
        lst.remove(min_num)
    else:
        break

print(f"The Second smallest number is {min(lst)}")
