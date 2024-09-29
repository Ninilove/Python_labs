# Write a program that will ask a student for their grade in 2 subjects
# First, we define all the subjects (variables) and assign them to a value, then using the input function that will prompt the user to enter their grades

Math = float(input("Enter your math grade:\t"))  
Science = float(input("Enter your science grade:\t"))
Art = float(input("Enter your art grade:\t"))
History = float(input("Enter your history grade here:\t"))
English = float(input("Enter your english grade here:\t"))

# using the sum function to calculate the average grade to determine the score of the student 

average_grade = sum([Math, Science, Art, History, English]) /5

# The print statement will display the average score of the student and round it to 2 decimal points

print (f"Your average grade is: {average_grade:.2f}")

if average_grade > 90:
    print("Your grade is A, Great job! Keep up the excellent work!!")

elif average_grade > 80:
    print("Your grade is B, You're doing well here! With a little more focus, you can push this up to an A!!")
    
elif average_grade > 70:
    print ("Your grade is C, You're holding steady, but there's definitely room for improvement!!")
    
elif average_grade > 60:
    print ("Your grade is D, This grade shows you're struggling. It might help to revisit some concepts or seek additional support!!")
    
    
else: 
    print ("Your score is E, Sorry, you have failed. Don't get discouraged, just practice more and seek help!!")
