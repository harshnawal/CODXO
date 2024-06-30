from random import randint

# Generate a random number (let's say between 1 and 10)
number = randint(1, 10)

# Get the number of chances from the user
chance = int(input("Enter the number of chances: "))

# Loop for the number of chances
for i in range(chance):
    # Get the user's guess
    test = int(input("Enter your guess: "))
    
    # Check if the guess is correct
    if number == test:
        print("You got it. The correct number is", str(test))
        break
    else:
        # If not the last chance, prompt to try again
        if i != chance - 1:
            print("Wrong number. Try again.")
        # If the last chance, print a consolation message
        else:
            print('Better luck next time.')
