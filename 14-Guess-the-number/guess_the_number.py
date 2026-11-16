
"""
Number Guessing Game

The computer generates a random number between 1 and 100.
The player tries to guess the number, receiving hints
until the correct number is found.
"""

# Import the random module to generate a random number
import random


def main():
    """Run the number guessing game."""

    # Generate a random secret number between 1 and 100
    secret = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    # Display the game instructions
    print("I'm thinking of a number between 1 and 100")

    # Continue asking until the player guesses correctly
    while True:

        # Get the player's guess
        guess = int(input("Your guess: "))

        # Increase the attempt counter
        attempts += 1

        # Give a hint if the guess is too low
        if guess < secret:
            print("Higher!")

        # Give a hint if the guess is too high
        elif guess > secret:
            print("Lower!")

        # The player guessed the correct number
        else:
            print(f"Correct! You got it in {attempts} guesses.")
            break


# Start the game when the script is executed directly
if __name__ == "__main__":
    main()
