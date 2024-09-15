import random

def ask_user(prompt, low=0, high=100):
    """Prompts the user to input a number between low and high (inclusive)."""
    while True:
        try:
            user_input = int(input(prompt))
            if low <= user_input <= high:
                return user_input
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Please enter a valid integer number.")


def main():
    print("Welcome to the Number Guessing Game!")
    random_number = random.randint(0, 100)
    print("I'm thinking of a number between 0 and 100. Can you guess it?")
    
    tries = 0
    
    while True:
        user_number = ask_user("Your guess: ")
        tries += 1
        
        if user_number == random_number:
            print(f"CONGRATULATIONS! You guessed the number in {tries} tries.")
            break
        elif user_number < random_number:
            print("Too low! Try a bit higher.")
        else:
            print("Too high! Try a bit lower.")
    
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay in ['yes', 'y']:
        main()  # Start a new game
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()
