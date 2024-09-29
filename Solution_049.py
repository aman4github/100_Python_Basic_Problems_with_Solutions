# Write a Python program to calculate the standard deviation of a list of numbers.

lst = [1, 2, 3, 4, 5]
squared_diff_lst = []
total = 0

for i in lst:
    total += i

mean = total // len(lst)
avg_total = 0

for i in lst:
    squared_diff_lst.append((i - mean)**2)
    avg_total += (i - mean)**2

avg = avg_total // len(squared_diff_lst)

print(f"Standard Deviation is {avg ** 0.5}")
