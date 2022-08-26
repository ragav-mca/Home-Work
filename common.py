#Input is two strings. Find all the chars that are in both strings. 

s1 = input("Enter first string: ") # Enter two input strings and store it in separate variables.
s2 = input("Enter second string: ")
errmsg = "No common chars" #initializing an variable for printing errmsg and common characters
commonChars = ""

for i in range(0, len(s1)): #using for loop and initializing a loop variable and assigning the value of s1[i]
    s1char = s1[i]
    for j in range(0, len(s2)): #using nested for loop and initializing a loop variable and assigning the value of s2[j]
        s2char = s2[j]
        if(s1char == s2char): #if statement for comparing two looping variables and if equals then add and print the string of commonChars += s1char
            commonChars += s1char
print(commonChars)
if(len(commonChars) == 0): #if it equals to 0 then print "No common chars"
    print(errmsg)
