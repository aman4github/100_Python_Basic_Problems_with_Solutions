# Write a Python program to calculate the compound interest.

p = int(input("Enter total amount : "))
roi = float(input("Enter the rate of interest : "))
n = int(input("Enter the number of time that the interest is compounded : \nEnter 1 to get annually\nEnter 2 to get Semi-Annually\nEnter 3 to get Quaterly\nEnter 4 to get Monthly\nEnter Your Choise : "))
t = int(input("Enter the number of year : "))

if n == 1:
    print(f"Total amount with compound interest will be {p * (1 + ((roi / 100) / 1)) ** (1*t)}")
elif n == 2:
    print(f"Total amount with compound interest will be {p * (1 + ((roi / 100) / 2)) ** (2*t)}")
elif n == 3:
    print(f"Total amount with compound interest will be {p * (1 + ((roi / 100) / 4)) ** (4*t)}")
elif n == 4:
    print(f"Total amount with compound interest will be {p * (1 + ((roi / 100) / 12)) ** (12*t)}")
else:
    print("Please choose a valid choise")
    