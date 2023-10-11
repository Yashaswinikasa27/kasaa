import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print(f"Can you guess the secret number between 1 and 100? You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__=="__main__":
     guess_the_number()
     