"""
We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
"""

clg_1 = input("Enter College 1: ") #getting the three colleges
clg_2 = input("Enter College 2: ")
clg_3 = input("Enter College 3: ")

print(clg_1) #printing the three colleges
print(clg_2)
print(clg_3)

clg1_cutoff = int(input("Enter the College 1 cutoff mark: ")) #getting cutoff marks for three clg's
clg2_cutoff = int(input("Enter the College 2 cutoff mark: "))
clg3_cutoff = int(input("Enter the College 3 cutoff mark: "))

print(clg1_cutoff) #printing those cutoff marks for three clg's
print(clg2_cutoff)
print(clg3_cutoff)


sub1 = int(input("Enter the subject 1 mark: ")) #getting five subject marks
sub2 = int(input("Enter the subject 2 mark: "))
sub3 = int(input("Enter the subject 3 mark: "))
sub4 = int(input("Enter the subject 4 mark: "))
sub5 = int(input("Enter the subject 5 mark: "))

avg = ((sub1) + (sub2) + (sub3) + (sub4) + (sub5)) / 5 #finding the average

if (avg > clg1_cutoff): #Condition for checking cutoff mark for three colleges
    if(avg > clg2_cutoff):
        if(avg > clg3_cutoff):
            print("Eligible for: ", clg_1, clg_2, clg_3)
        else:
            print("Eligible for: ", clg_1, clg_2) #if the third if condition fails then print clg1 and clg2
    elif(avg > clg3_cutoff): #if the second if condition fails then check with clg3 cutoff and it passes then print clg1 and clg3
        print(clg_1, clg_3)
    else:
        print(clg_1) #if the third if condition also fails then print clg1 alone
elif(avg > clg2_cutoff): #if the first if condition fails then it directly comes to this condition and checks with clg2 cutoff
    if(avg > clg3_cutoff): #and if above elif condition passes then it checks with clg3 cutoff if it passes then it prints clg2 and clg3
        print(clg_2, clg_3)
    else:
        print(clg_2) #if clg3 cutoff fails then it prints clg2 alone
elif(avg > clg3_cutoff): #if the above clg1 and clg2 condition fails then it comes to clg3 and checks if it passes then it prints clg3
    print(clg_3)
else:
    print("Not Eligible") #if the above all condition fails then it prints not eligible 





