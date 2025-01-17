import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. You have 5 attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_number()
