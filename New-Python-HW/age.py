"""
Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name. 
Ask what year they were born.  get the year from the user. Print 'You are <age> years old'.

"""
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
present_year = int(input("Enter the present year: "))
age = (present_year - birth_year)

print('Hello',name)
print(birth_year)
print(present_year)
print('You are' , age , 'years old')