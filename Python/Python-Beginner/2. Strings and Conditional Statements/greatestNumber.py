#WAP to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nt Number: "))
num3 = int(input("Enter 3rd Number: "))

if (num1 > num2 and num1 > num3):
    print("1st Number is the greatest")
elif (num2 > num1 and num2 > num3):
    print("2nd Number is the greatest")
else:
    print("3rd Number is the greatest")