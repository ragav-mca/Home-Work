"""
Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name and print 'Hello', user's name. 
Ask what year they were born.  get the year from the user. 
Calculate if the user is going to elementary school, middle school, highschool or college.
(hint - use if/elif)
"""
name = input("Enter your name: ")
birth_year = int(input("Enter the year you born: "))
present_year = int(input("Enter the present year: "))
age = (present_year - birth_year)

print("Hello", name)
print(birth_year)
print(present_year)
print(age)

if (age <= 10):
    print("The", name ,"is going to elementary school")
elif (age >= 11 and age <= 13):
    print("The", name ,"is going to middle school")
elif (age >= 14 and age <= 17):
    print("The", name ,"is going to high school")
elif (age >= 18 and age <= 21):
    print("The", name ,"is going to college")
else:
    print("None")



