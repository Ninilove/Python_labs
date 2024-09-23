# Write a program that will ask for a word and reverse the word

# The input function will let the user say something
word = (input('say something:\n'))

# Using the slicing method (string[::-1])to reverse the world the user will choose

reverse_word = (word[::-1])

print (f'Your word is:{word}, and the reverse is:{reverse_word}.')