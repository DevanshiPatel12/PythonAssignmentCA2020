# Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “c” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.

user = int(input("Enter any number : "))
if user % 3 == 0 and user % 5 == 0:
    print("Consultadd Python Training")
elif user % 3 == 0:
    print("Consultadd")
elif user % 5 == 0:
    print("c")
else:
    print("Number is not divisible by 3 or 5")