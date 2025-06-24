correct_username = "user100"
correct_password = "pass4121"

print("Welcome to the website login page")
print("....................................")

username =  input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("\nlogin successful!")
    print("redirecting page...\n")
    print("Welcome to the website homepage")
    print("Welcome,", username)
else:
    print("login failed, invalid username or password")
    print("Please try again")


import time

count = int(input("Enter starting number: "))

while count > 0:
    print(count)
    time.sleep(1)
    count -= 1

print("Time's up!")


import random

number = random.randint(1, 20)
attempts = 5

while attempts > 0:
    guess = int(input("Guess a number between 1 and 20: "))

    if guess == number:
        print("Correct! You win!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("You lost! The number was:", number)