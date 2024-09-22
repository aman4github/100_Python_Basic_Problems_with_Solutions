# Write a Python program to find the intersection of two lists

lst1 = [10, 20, 30, 30]
lst2 = [30, 40, 50]

# Method 1 
print(f"Intersection of both list is {list(set(lst1).intersection(set(lst2)))}")

# Method 2 
print(f"Intersection of both list is {list(set(lst1) & set(lst2))}")

# Method 3 
intersec_lst = []

for i in lst1:
    if i in lst2:
        if i not in intersec_lst:
            intersec_lst.append(i)

print(f"Intersection of both list is {intersec_lst}")
