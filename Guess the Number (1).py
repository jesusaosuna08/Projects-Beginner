
import random

correct_number = 8

guess_number = (int(input("What is your guess?: ")))


#while guess_number != correct_number:
    #if guess_number == correct_number:
        #print("Correct!")
    #else:
        #print("Wrong!")

# This code is wrong, and it gave me an infinity of "Wrong!"s if I inputted the wrong number
# At least this is partly due to the fact that I never request for additional input in this block of code

while guess_number != correct_number:
    print("WRONG")
    guess_number = (int(input("What is your guess?: ")))

if guess_number == correct_number:
    print("Correct!")

# This is better, but I still want the program to tell me that I am "Wrong!"


random_generated_number = random.randint(0,10)

my_guess = (int(input("What is your guess?: ")))

while my_guess != random_generated_number:
    print("WRONG!!!")
    my_guess = (int(input("What is your guess?: ")))

if my_guess == random_generated_number:
    print("You got it!")










