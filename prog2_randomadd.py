# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import time
import random
# generate two random numbers to add (0 to 99)
def randAdd():
    firstNum = random.randint(0,99)
    secondNum = random.randint(0,99)
    randAns = firstNum + secondNum
    time.sleep(1.5)
    print(f"What will be the sum if {firstNum} is added to {secondNum}?")
    return randAns
# evaluate if the user has the correct answer
def userAns():
    global randAns
    randAns = randAdd()
    time.sleep(1)
    userAns = int(input("Enter answer: "))
    return randAns == userAns
# ask 10 questions and display the score summary