number = 10
print("I'm thinking of a number...")

while True:
    guess_str = input("What number am I thinking of? (Enter 'q' to quit) ")

    if guess_str.lower() == 'q':
        print(f"The number was {number}. Goodbye!")
        break
    else:
        try:
            guess = int(guess_str)
            if guess == number:
                print("Congratulations! You guessed the right number.")
                break
            elif guess < number:
                print("Sorry! Your guess is too low. Try again.")
            else:
                print("Sorry! Your guess is too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
