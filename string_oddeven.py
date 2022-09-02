#Input a string. 
#    Print all the chars that are in Odd index - eg intput - abcd, output bd
#    Print all the chars in the even index in reverse order - eg input abcd output ca
inputstring = input("Enter your string: ")
for charindex in range(1,len(inputstring),2):
    print(inputstring[charindex])
print("End of first forloop")
for charindex in range(len(inputstring)-2,-1,-2):
    print(inputstring[charindex])
print("End of second forloop")
    
