"""
Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or mininum.
Find the answer and print.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    maximum = num1
elif (num2 >= num1) and (num2 >= num3):
    maximum = num2
else:
    maximum = num3

if (num1 <= num2) and (num1 <= num3):
    minimum = num1
elif (num2 <= num1) and (num2 <= num3):
    minimum = num2
else:
    minimum = num3

user_choice = input("Enter max or min : " )
if (user_choice == "max"):
    print("The maximum number is: ", maximum)
elif (user_choice == "min"):
    print("The minimum number is: ", minimum)
else:
    print("None")


