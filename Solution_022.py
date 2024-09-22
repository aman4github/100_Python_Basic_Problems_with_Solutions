# Write a Python program to remove duplicates from a list.

lst = [10, 30, 90, 20, 50, 10, 30]

print(f"List before removing all duplicate numbers : {lst}")

# Method 1 
print(f"List after removing all duplicate numbers : {set(lst)}")

# Method 2 
lst = [10, 30, 90, 20, 50, 10, 30]
unique_lst = []

for i in lst:
    if i not in unique_lst:
        unique_lst.append(i)

print(f"List after removing all duplicate numbers : {unique_lst}")
