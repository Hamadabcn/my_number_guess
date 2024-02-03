import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n\n           Welcome to the Number Guessing Game!🔮 🔮 🔮\n")
    print("\n          I'm thinking of a number between 1 and 100.🤔 \n")

    while True:
        guess = int(input("\nTake a guess: 🙏  "))
        attempts += 1

        if guess < secret_number:
            print("\nToo low! Try again.⬆️\n")
        elif guess > secret_number:
            print("\nToo high! Try again.⬇️\n")
        else:
            print(f"\nCongratulations! You found the secret number in {attempts} attempts.\n")
            break

# use a variable to store the player's choice
play_again = "y"

# use a while loop to repeat the game until the player chooses to quit
while play_again.lower() == "y":
    # call the number guessing game function
    number_guessing_game()
    # ask the player if they want to play again
    play_again = input("\nDo you want to play again? (y/n) ")
    # if the player chooses to quit, print a farewell message
    if play_again.lower() == "n":
        print("\nThank you for playing. Have a nice day!\n")
        