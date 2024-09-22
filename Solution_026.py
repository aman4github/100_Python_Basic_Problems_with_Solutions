# Write a Python program to find the union of two lists.

lst1 = [10, 20, 30, 30]
lst2 = [30, 40, 50]

# Method 1 
print(f"Union of both lists is = {list(set(lst1).union(lst2))}")

# Method 2
print(f"Union of both lists is = {list(set(lst1) | set(lst2))}")

# Method 3

unique_lst = []

union_lst = lst1 + lst2

for i in union_lst:
    if i not in unique_lst:
        unique_lst.append(i)

print(f"Union of both lists is = {unique_lst}")
