"""
We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
"""

College_1 = input("Enter College 1: ") #getting the three colleges
College_2 = input("Enter College 2: ")
College_3 = input("Enter College 3: ")

print(College_1) #printing the three colleges
print(College_2)
print(College_3)

sub1 = int(input("Enter the subject 1 mark: ")) #getting five subject marks
sub2 = int(input("Enter the subject 2 mark: "))
sub3 = int(input("Enter the subject 3 mark: "))
sub4 = int(input("Enter the subject 4 mark: "))
sub5 = int(input("Enter the subject 5 mark: "))

avg = ((sub1) + (sub2) + (sub3) + (sub4) + (sub5)) / 5 #finding the average

if(avg > 98): #Calculating the eligibility
    print("The Eligible Colleges are: ", College_1 , College_2 , College_3)
elif(avg > 96):
    print("The Eligible Colleges are: ", College_2 , College_3)
elif(avg > 94):
    print("The Eligible Colleges are: ", College_3)
else:
    print("You are not Eligible")


