"""
In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
  Use functions.

"""
from pickle import FALSE


def betweenletters(word,letter):
  """
  firstletter = -1
  lastletter = -1
  foundletter = FALSE
  firstletter = word.find(letter)
  lastletter = word.rfind("A")
  """
inputstring =input("Enter the string: ")
first_index = -1
last_index = -1
err_msg = "a is not found"
for index in range(0,len(inputstring)):
    if(inputstring[index == "a"]):
        first_index = index
        break
if(first_index != -1):
    for index in range(len(inputstring)-1,-1,-1):
        if(inputstring[index == "a"]):
           last_index = index
           break

if(first_index != -1 and last_index != -1):
    print("a first occur in index of: ", first_index)
    print("a last occur in index of: ", last_index)
else:
    print(err_msg)
