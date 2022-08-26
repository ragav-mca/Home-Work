#In the input, find the first A and last A, print all the letters between these two A.
str1 = input("Enter the first string: ")
for i in range(0,len(str1)):
    str1char = str1[i]
    if str1char[0 & -1] == 'a':
        print(str1char[1:-1])
        



