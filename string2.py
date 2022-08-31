#Input is two strings. Find all the chars that are in both strings. 

yourword = input("Enter your word: ") #inputs
yourchar = input("Enter your character you want to find: ")
char_count = 0 
print(yourword)
strlen = (len(yourword)) #finding the length of the string
for word_index in range(0,strlen): #loop in range starting index to last index
    if(yourchar == yourword[word_index]): #to find the position of the character index
        char_count += 1 #incrementing the char count if the condition equals
print(char_count) #printing the character count