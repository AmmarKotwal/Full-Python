# Multiple Choice Python Quiz

score = 0  # Initialize score

print("Welcome to the Python Quiz!")
print("Please type A, B, C or D for each answer.\n")

print("1. Which of the following is used to define a function in Python?")
print("A. function\nB. define\nC. def\nD. fun")
ans1 = input("Your answer: ").strip().upper()
if ans1 == "C":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is C. def\n")

print("2. What is the correct file extension for Python files?")
print("A. .pt\nB. .py\nC. .pyt\nD. .pyth")
ans2 = input("Your answer: ").strip().upper()
if ans2 == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is B. .py\n")

print("3. What is the output of: print(3 * '2') ?")
print("A. 6\nB. 222\nC. 32\nD. Error")
ans3 = input("Your answer: ").strip().upper()
if ans3 == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is B. 222\n")

print("4. Which of these is a Python tuple?")
print("A. [1, 2, 3]\nB. {1, 2, 3}\nC. (1, 2, 3)\nD. <1, 2, 3>")
ans4 = input("Your answer: ").strip().upper()
if ans4 == "C":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is C. (1, 2, 3)\n")

print("5. Which keyword is used to start a loop in Python?")
print("A. for\nB. loop\nC. repeat\nD. iterate")
ans5 = input("Your answer: ").strip().upper()
if ans5 == "A":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is A. for\n")

print("Quiz Completed!")
print(f" Your Total Score: {score} out of 5")


if score == 5:
    print("Excellent! You're a Python pro!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("Keep learning. Practice makes perfect!")


