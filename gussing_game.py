import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guessed = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while not guessed:
        try:
            # Get the user's guess
            user_guess = int(input("Enter your guess: "))

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it right. The number was {number_to_guess}.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guessing_game()
