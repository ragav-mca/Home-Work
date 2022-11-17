#Get a movie name. Find out how many words are in that movie. 

movie_name = input("Enter the movie name: ")
print("The movie name is: ", movie_name)

count_words = movie_name.count(" ") + 1
print("The number of word in the movie are: ", str(count_words))