# Write a Python program to check if a year is a leap year.

year = int(input("Enter the year : "))

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(f"Year {year} is a Leap Year")
else:
    print(f"Year {year} is not a Leap Year")
    