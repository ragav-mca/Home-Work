"""
Get the marks for 5 subjects from the student. Calculate the average values. 
Calcualte if the student got A grade (avg > 90) or B grade (avg > 80) or C grade (avg > 70) or fail.
"""
sub1 = int(input("Enter marks of first subject: ")) #getting five subject marks
sub2 = int(input("Enter marks of second subject: "))
sub3 = int(input("Enter marks of third subject: "))
sub4 = int(input("Enter marks of fourth subject: "))
sub5 = int(input("Enter marks of fifth subject: "))

avg = (sub1 + sub2 + sub3 + sub4 + sub5) /5 #calculating avg of five subjects

if (avg > 90): #calculating grades
    print("Grade: A")
elif (avg > 80):
    print("Grade: B")
elif (avg > 70):
     print("Grade: C")
else:
    print("Fail")

