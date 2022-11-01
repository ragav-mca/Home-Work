"""
Get the marks for 3 subjects from the students.
 If the marks is greater than 75 in any two subjects, then print Pass and also print the subject where the marks in > 75
 If the marks is greater than 60 in all three subjects, then print pass.
 if the above condition is not met, print fail.
"""

sub1 = input("Enter the first subject mark: ") #getting three subject marks
sub2 = input("Enter the second subject mark: ")
sub3 = input("Enter the third subject mark: ")

if ((int(sub1) > 75) and (int(sub2) > 75) and (int(sub3) > 75) ): #condition for checking if three sub > than 75 
    print("Pass")
elif (int(sub1) > 75 and int(sub2) > 75 or int(sub1) > 75 and int(sub3) > 75 or int(sub2) > 75 and int(sub3) > 75): #condition for checking if any two sub > than 75 
    print("Pass")
    if(int(sub1) > 75): #condition for printing the sub > than 75
        print("The subject greater than 75: ", sub1)
    elif(int(sub2) > 75):
        print("The subject greater than 75: ", sub2)
    elif(int(sub3) > 75):
        print("The subject greater than 75: ", sub3)
elif (int (sub1) > 60 and int (sub2) > 60 and int (sub3) > 60): #condition for checking if all three sub > than 60
    print("Pass")
else:
    print("Fail") #if all above conditions gets fail then print fail
