"""
Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long.
"""
import re #using RegEx method to find
password = input("Enter the password: ") #Inputs
alphabet = ""
number = -1
spl_char = "!@#$%"
x = True #using boolean to check 
while x:
#to check if only alphabets or only numbers or only special chars
    if re.search("[a-z]",password): 
        print("Your password is weak") 
        break
    elif re.search("[0-9]",password):
        print("Your password is weak")
        break
    elif re.search("[!$#@]",password):
        print("Your password is weak")
        break
#to check and print ok if atleast one alphabet, one number and one special char
    elif re.search(alphabet >=1 and number >=1 and spl_char >= 1):
        print("Your password is ok")
        break
# to check and print very strong if it prints all characters with at least 16 count
    elif re.search("[a-z]">=3 and"[0-9]">=2 and spl_char >=1,password):
        print("Your password is strong")
        break
else:
    if password < 8:
        print("Password is Invalid")
    
        


    
    
    """
    bool = password.isalpha() or password.isnumeric() 
    if(bool == True):
       print("The password is weak")
       break

    bool = re.search("[!@#$%&*]",password)
    if(bool == True):
        print("The password is weak")
        break

    bool = password.isalpha([1]) and password.isnumeric(1)
    if (bool == True):
        print("The password is ok") 

    bool = password.isalpha >=3 and password.isnumeric >=3 
    if(bool == True):
        print("The password is strong")

    bool = (password.isalpha >=3 and password.isnumeric >=3) >=16
    if (bool == True):
        print("The password is very strong")

    else:
        print("Invalid password")
        """  


    

