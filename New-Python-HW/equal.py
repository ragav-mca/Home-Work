"""
Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
    until the length is equal. 
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cataa, arrow (length is equal by adding a)
"""
name1 = input("Enter the name 1: ")
name2 = input("Enter the name 2: ")

print(name1)
print(name2)

strlen1 = len(name1)
strlen2 = len(name2)

print(strlen1)
print(strlen2)

max = 0
min = 0

if(strlen1 > strlen2):
    max = name1
    min = name2
elif(strlen2 > strlen1):
    max = name2
    min = name1
else:
    print("Both strings are equal")

print("The maximum of two strings is: ", max)
print("The minimum of two strings is: ", min)

x = "a"
y = len(max)

for i in range(0,y):
    min = min + "a"
print(min)
        
#min = min + x * y
  #print("The string after equalling with a: ", min + x * y) break:  
#print("The string after equalling with a: ", str(min))  




