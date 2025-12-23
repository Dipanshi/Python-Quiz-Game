print("Welcome to the Python Quiz Game!")
score=0

#Checking if user wants to play
play= input("Do you want to play? (yes/no): ")
if play.lower() != "yes":
    print("Maybe next time! Goodbye.")
    exit()

#Quiz Questions
answer= input('1. What does "PEP" stand for? ')
if answer.lower() == "python enhancement proposal":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Python Enhancement Proposal'.")

answer= input('2. What is the output of print(2 ** 3 ** 2)? ')
if answer.lower() == "512":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is '512'.")

answer= input('3. Which Python data type is mutable? ')
if answer.lower() in ["list","dict","dictionary","set"]:
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is any from list, dictionary, set'.")

answer= input('4. Which keyword is used to define a class in Python? ')
if answer.lower() == "class":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'class'.")


answer= input('5. Which built-in function returns the number of items in an iterable? ')
if answer.lower() == "len":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'len'.")

print("Your correct answers are", score, "out of 5.")
print("Your score percentage is", (score/5)*100, "%.")
print("Thank you for playing the Python Quiz Game!")

