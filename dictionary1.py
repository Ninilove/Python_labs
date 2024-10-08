# Create an English to French translator program.
# The program takes a word from the user as an input and translates it using a dictionary data type as a vocabulary
# Please add the translation of 'prune' in your homework
# If the word is not in the code vocabulary print ({word} is not in my memory)
# The user will select the language they would like to translate to

# first we define the words in English and their translation in French
word_english_french = {
    "good morning": "bonjour",
    "good night": "bonne nuit",
    "i am sorry": "je suis désolé",
    "i love you": "je t'aime",
    "how are you": "comment ça va",
    "prune": "élaguer",
    "what's your name": "comment tu t'appelles",
    "East coast the best coast": "la côte Est est la meilleure côte",
}

# Prompt the user to say something
text_to_translate = input("Say something in English:\n")

# Use the get method to retrieve the translation
translation = word_english_french.get(text_to_translate)

# Check if translation is available and print the result
if translation:
    print(f"The translation in French is: {translation}")
else:
    print("The word is not in my memory. Please help me find it.")
