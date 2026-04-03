import random

def start_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to Number Guessing Game!")
    
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

start_game()