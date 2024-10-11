# Write a Python program to find the second most frequent character in a string.

def freq(str):
    max_freq = str[0]
    lst = []
    for i in str:
        if str.count(max_freq) < str.count(i):
            max_freq = i
            lst.clear()
            if i not in lst:
                lst.append(i)
        elif str.count(max_freq) == str.count(i):
            max_freq = i
            if i not in lst:
                lst.append(i)
    return lst


str = input("Enter the string : ")
str2 = ""

most_freq = freq(str)

for i in str:
    if i not in most_freq:
        str2 += i

print(f"The Second most frequent character is {freq(str2)}")
