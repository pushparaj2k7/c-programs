import random

# Random number between 1 and 99
secret_number = random.randint(1, 99)

# Guess counter
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 99")

while True:
    guess = int(input("Enter your guess: "))
    
    attempts += 1

    if guess == secret_number:
        print("Correct! You guessed the number.")
        print("You guessed it in", attempts, "attempts.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print(" Too high! Try again.")