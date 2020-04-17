# Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
#            		counter=1
# 		While counter <= 5:
# 			print(“Type in the”, counter, “number”
# 			counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not).
# If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.

L = 10
count = 1
while count <= 5:
    number = int(input("Guess the lucky number: "))
    print("Your guessed number is : ", number," and", count, " try.")
    if number == L:
        print("Good Guess !!")
        count = count + 1
    else:
        print("Try again !")
        count = count + 1
        continue
print("Game Over!")