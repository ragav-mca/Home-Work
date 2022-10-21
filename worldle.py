"""
Code the game Wordle (text based. Instead of color, use letters - G for green, Y for yellow and B for grey). 
https://www.nytimes.com/games/wordle/index.html
Start with 3 letter word. If user guesses the word correctly, then 4 letters and then 5 letters. 

"""

actual_word = "ragav"
input_word = input("Enter the word: ")
print("Input is: ", input_word)
temp_list = []
check_string = ["red"] * len(actual_word)

for char in range(len(input_word)):
    if actual_word[char] == input_word[char]:
        check_string[char] = "green"
        temp_list.append(actual_word[char])

for char in range(len(input_word)):
    if input_word[char] in actual_word and check_string[char] != "green" and input_word[char] != "green" and input_word[char] not in temp_list:
        check_string[char] = "yellow"

print("Output is : ", ''.join([str(i) for i in check_string]))


