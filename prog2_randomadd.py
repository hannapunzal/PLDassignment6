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
def userAsk():
    name = input("Hi! Enter your name to proceed: ")
    time.sleep(1)
    print(f"Hi {name}! You are going to answer 10 random addition questions. Let's get you started! ☺")
    currentScore = 0
    for i in range(10):
        rightAns = userAns()
        if rightAns:
            currentScore += 1
            print(f"Congratulations, {name}! You got the correct answer!")      
        else:
            currentScore = currentScore    
            print(f"Sorry, the correct answer is {randAns}.") 
    time.sleep(1)
    print("Calculating final score...")
    time.sleep(2)
    if currentScore >=7:
        print(f"{name}, your final score is {currentScore}/10. That's great! \nHope to see you again next time! ♥")
    if currentScore >=5 and currentScore <7:
        print(f"{name}, your final score is {currentScore}/10. Not bad! \nHope to see you again next time! ♥")
    if currentScore <5:
        print(f"{name}, your final score is {currentScore}/10. Nice try! Your arithmetic skills need improvement though... \nHope to see you again next time! ♥")
    
    print("End")

userAsk()