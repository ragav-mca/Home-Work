"""
Get the marks for 3 subjects from the students.
 If the marks is greater than 75 in any two subjects, then print Pass and also print the subject where the marks in > 75
 If the marks is greater than 60 in all three subjects, then print pass.
 if the above condition is not met, print fail.
"""
#getting three subject names
sub1 = input("Enter subject 1: ")
sub2 = input("Enter subject 2: ")
sub3 = input("Enter subject 3: ")

print(sub1)
print(sub2)
print(sub3)

#getting three subject marks
sub1_mark = int(input("Enter the first subject mark: ")) 
sub2_mark = int(input("Enter the second subject mark: "))
sub3_mark = int(input("Enter the third subject mark: "))

#condition for checking any two subjects above 75
if (int(sub1_mark) > 75 and int(sub2_mark) > 75 or int(sub1_mark) > 75 and int(sub3_mark) > 75 or int(sub2_mark) > 75 and int(sub3_mark) > 75): 
    print("Pass")

#condition for checking any two subjects above 60
elif(int (sub1_mark) > 60 and int (sub2_mark) > 60 and int (sub3_mark) > 60): 
    print("Pass")

#if above two condition fails then it prints fail
else:
    print("Fail") 

#condition for printing the subject name above 75
sub = []
if sub1_mark > 75:
    sub.append(sub1)
if sub2_mark > 75:
    sub.append(sub2)
if sub3_mark > 75:
    sub.append(sub3)
print("Subject greater than 75: ",sub)

#condition if sub==0
if (len(sub) == 0):
    print(None)

