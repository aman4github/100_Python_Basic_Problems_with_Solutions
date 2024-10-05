# Write a Python program to calculate the simple interest.

p = int(input("Enter the Principal amount : "))
roi = float(input("Enter the rate of interest : "))
t = int(input("Enter the number of year : "))

print(f"Simple interest with principal will be {(p + (p * roi * t) / 100)}")
