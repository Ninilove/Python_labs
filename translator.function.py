# write a program that converts km to miles
# 1km = 1.6 miles

#def km_to_miles(km):
    #miles = km * 0.621371
    #return miles

#kilometers = float(input('Enter a distance in kilometers: '))
#miles = km_to_miles (kilometers)
#print (f" {kilometers} kilometers is equal to {miles} miles.")

# first we define the words in English and their translation in French
# word_english_french = {
#     "good morning": "bonjour",
#     "good night": "bonne nuit",
#     "i am sorry": "je suis désolé",
#     "i love you": "je t'aime",
#     "how are you": "comment ça va",
#     "prune": "élaguer",
#     "what's your name": "comment tu t'appelles",
#     "East coast the best coast": "la côte Est est la meilleure côte",
# }

# # Prompt the user to say something
# text_to_translate = input("Say something in English:\n")

# # Use the get method to retrieve the translation
# translation = word_english_french.get(text_to_translate)

# # Check if translation is available and print the result
# if translation:
#     print(f"The translation in French is: {translation}")
# else:
#     print("The word is not in my memory. Please help me find it.")

# First describe the list we will pull the translation from

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
# using the def function we create a checklist function with the parameter word to check

def checklist(word_to_check):
    translation = word_english_french.get(word_to_check)
    return translation

# This line of code will prompt the user to say something in English

text_to_translate = input ("Say something in english: \n")


translation = checklist(text_to_translate)
# Using the if statement so that if the user says something that's not in dictionary he will get a different message
if translation:
    print (f'The translation in French is: {translation}')
    
else:
    print ("The word is not in my memory. Please help me find it.")