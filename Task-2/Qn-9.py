# Read the two parts of the question below:
# Write a program such that it asks users to “guess the lucky number”.
# If the correct number is guessed the program stops, otherwise it continues forever.

# Modify the program so that it asks users whether they want to guess again each time.
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing.
# The program stops if the user guesses the correct number or answers “no”.
# (The program continues as long as a user has not answered “no” and has not guessed the correct number)

num = 5
while True:
    user = int(input("guess the lucky number: "))
    if user == num:
        print("you guessed the correct number")
        break
    else:
        print("incorrect")
        continue


# Modified Program
L = 10
while True:
    number = int(input("Guess the lucky number : "))
    if number == L:
        print("You guessed the correct number.")
    else:
        print("Incorrect lucky number.")
        answer = input("Do you want to guess again? type Yes or No : ")
        if answer == 'Yes' or answer == 'yes':
            continue
        else:
            print("Game over")
            break
