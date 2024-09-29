# Write a Python program to find the mode of a list of numbers.

lst = [1, 2, 3, 1, 5, 5, 6, 2, 6]

freq_dict = {}

mode_lst = []

for i in lst:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1

print(freq_dict)

max_value = 0
for key, value in freq_dict.items():
    if max_value < value:
        max_value = value
        mode_lst.clear()
        mode_lst.append(key)
    elif max_value == value:
        max_value = value
        mode_lst.append(key)

print(f"Mode of this list is {mode_lst}")
