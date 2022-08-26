# Ask your friend all the movies s/he watched recently. List all the movies that you both have watched,
# only the movies you watched, and only the movies your friend  watched.

s1 = input("Enter the movies watched by the friend recently: ")
s2 = input("Enter all the movies that you both watched: ")
s3 = input("Enter only the movies watched by you: ")
s4 = input("Enter only the movies your friend watched: ")
commonChars = ""
errmsg = "No same movie has been watched by both"

for i in range(0,len(s1)):
    s1char = s1[i]
    for j in range(0,len(s2)):
        s2char = s2[j]
        if s1char == s2char:
            commonChars += s2char
print(s3)
print(s4)
print(commonChars)
if(len(commonChars) == 0):
    print(errmsg)


