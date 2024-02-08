number = 10
max_attempts = 3  # Set the maximum number of guesses
print("I'm thinking of a number...")
attempts = 0
while attempts < max_attempts:
    guess_str = input(f"What number am I thinking of? (Enter 'q' to quit) You have {max_attempts - attempts} guesses left: ")
    if guess_str.lower() == 'q':
        print(f"The number was {number}. Goodbye!")
        break
    else:
        try:
            guess = int(guess_str)
            attempts += 1

            if guess == number:
                print("Congratulations! You guessed the right number.")
                break
            else:
                if attempts < max_attempts:
                    print(f"Sorry! Your guess is incorrect. You have {max_attempts - attempts} guesses left. Try again.")
                else:
                    print(f"Sorry! Your guess is incorrect. The number was {number}. You're out of guesses. Goodbye!")
                    break
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
