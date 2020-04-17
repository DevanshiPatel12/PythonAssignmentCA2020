# In the previous question, insert “break” after the “Good guess!” print statement.
# “break” will terminate the while loop so that users do not have to continue guessing after they found the number.
# If the user does not guess the number at all, print “Sorry but that was not very successful”.

L = 10
count = 1
while count <= 5:
    number = int(input("Guess the lucky number: "))
    print("Your guessed number is : ", number," and", count, " try.")
    if number == L:
        print("Good Guess !!")
        break
    else:
        print("Try again !")
        count = count + 1
        continue
print("Game Over!")