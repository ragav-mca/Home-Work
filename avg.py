#declaring the numbers
print("Input some integers to calculate their sum and average. Input 0 to exit.")
count = 0 #intializing the variables 
sum = 0
number = 1

while number != 0: #initializing while loop != 0 to end the block if the user enters 0
    number = int(input("Enter the Numbers: ")) # getting the numbers from the user
    sum = sum + number #calculating sum by adding each of the number in the list
    count += 1 #declaring the count as 1 to count each of the number

if count == 0: #printing the above condition
    print("Input some Numbers")
else:
    print("Average and Sum of the above numbers are: ", sum /(count-1), sum)

