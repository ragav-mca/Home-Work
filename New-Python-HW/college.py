"""
We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
"""
#getting the three colleges
clg_1 = input("Enter College 1: ") 
clg_2 = input("Enter College 2: ")
clg_3 = input("Enter College 3: ")

print(clg_1)
print(clg_2)
print(clg_3)

#getting cutoff marks for three clg's
clg1_cutoff = int(input("Enter the College 1 cutoff mark: "))
clg2_cutoff = int(input("Enter the College 2 cutoff mark: "))
clg3_cutoff = int(input("Enter the College 3 cutoff mark: "))

print(clg1_cutoff) 
print(clg2_cutoff)
print(clg3_cutoff)

eligible_clg = []

#getting five subject marks
sub1 = int(input("Enter the subject 1 mark: ")) 
sub2 = int(input("Enter the subject 2 mark: "))
sub3 = int(input("Enter the subject 3 mark: "))
sub4 = int(input("Enter the subject 4 mark: "))
sub5 = int(input("Enter the subject 5 mark: "))

#finding the average
avg = ((sub1) + (sub2) + (sub3) + (sub4) + (sub5)) / 5 

#Condition for checking cutoff mark 
if (avg > clg1_cutoff): 
    eligible_clg.append(clg_1)

if(avg > clg2_cutoff):
    eligible_clg.append(clg_2)

if(avg > clg3_cutoff):
    eligible_clg.append(clg_3)
    
print("The Eligible College are: ", eligible_clg)

#Condition for checking if the array is empty or < than the criteria
if (len(eligible_clg) == 0):
    print("Not Eligible")


