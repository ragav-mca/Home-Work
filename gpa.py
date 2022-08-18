credit = int(input("Enter the credit points: ")) #inputs
student_no = 0
subject_no = 0
mark = 0
for mark in range(1,4): #for getting three student and three subject marks
    student_no += 1
    subject_no += 1
    mark = int(input("Enter subject mark: "))
    print("student no", student_no, "subject no", subject_no, "mark", mark)

total_credits = credit * 3 #multiplying credit by no of subjects
gpa = (credit * mark + credit * mark + credit * mark) / total_credits #calculating gpa
print(credit)
print("Total Credits: ", total_credits)
print("Grade Point Average: ", gpa)

if mark == 100: #to know the grade of marks
    print("Grade: O")
elif mark >= 90:
    print("Grade: A+")
elif mark >= 80:
    print("Grade: A")
elif mark >= 70:
    print("Grade: B+")
elif mark >= 60:
    print("Grade: B")
elif mark >= 49:
    print("Grade: RA")
else:
    print("Withheld")

