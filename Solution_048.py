# Write a Python program to find the median of a list of numbers.

def median(lst):
    size = len(lst)
    if size % 2 == 0:
        return (lst[size // 2] + lst[(size // 2) - 1]) / 2
    else:
        return lst[size // 2]

odd_lst = [1, 2, 3, 4, 5]
even_lst = [4, 5, 6, 7]

print(f"Median of the Odd list is {median(odd_lst)}")
print(f"Median of the Even list is {median(even_lst)}")
