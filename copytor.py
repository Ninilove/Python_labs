# Write a file called copy which takes in a file name and a new file name and copies the contents of the first line into the second line

# The code snippet you provided is opening a file named 'story.txt' in write mode ('w'). It then
# writes multiple lines of text to the file. Each `file.write()` call appends the given text to the
# file. The text being written seems to be an excerpt from the story of Alice in Wonderland.

# step 1 is to write the content to story.txt
with open ('story.txt', 'w') as file :
    file.write ("Down the Rabbit-Hole\n")
    file.write ("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, `and what is the use of a book,' thought Alice `without pictures or conversation?\n")
    file.write ("So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.\n")
    file.write ("There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, `Oh dear! Oh dear! I shall be late!\n")
    file.write ("when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge.")
 
# step 2 is to define the copy function
def copy (source_file, target_file): # open the source file to read its content
    with open (source_file, 'r') as source:
        content = source.read()   # read the entire content of the source file
        
    
    with open (target_file, 'w') as target: # open the target file to write the content from the source file
        target.write(content) # write content to target file
        
# step 3 is to call the function

copy ('story.txt', 'story.copy.txt')  # the copy function calls to copy the contents from story.txt to story.copy.txt
        
        
        