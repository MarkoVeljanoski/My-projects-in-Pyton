import random

def guess_number():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break  # Correct guess, exit the loop
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_number()