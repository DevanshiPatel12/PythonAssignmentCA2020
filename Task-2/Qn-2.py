# Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
    # If User Enter 1 - Addition
    # If User Enter 2 - Subtraction
    # If User Enter 3 - Division
    # If USer Enter 4 - Multiplication
    # If User Enter 5 - Average
# Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
# Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “zsa”

# NOTE: At a time user can perform one action at a time.

a = int(input("1 Addition \n2 Subtraction \n3 Division \n4 Multiplication \n5 Average \nEnter number to choose option : "))
x, y = input("Enter two comma separated numbers to perform above action : ").split(",")
first = int(x)
second = int(y)
if a == 1:
    final = first + second
    print("Addition is : ", final)
elif a == 2:
    final = first - second
    print("Subtraction is : ", final)
elif a == 3:
    final = first / second
    print("Division is : ", final)
elif a == 4:
    final = first * second
    print("Multiplication is : ", final)
else:
    e,f = input("Enter another two comma separated numbers : ").split(",")
    first1 = int(e)
    second2 = int(f)
    final = (first + second + first1 + second2)/4
    print("Average is : ", final)

if final < 0:
    print("zsa")
