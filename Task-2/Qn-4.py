# Write a program in Python to break and continue if the following cases occurs:
    # If user enters a negative number just break the loop and print “It’s Over”
    # If user enters a positive number just continue in the loop and print “Good Going”

num = int(input("Enter any number : "))
while True:
    if num < 0:
        print("It's over")
        break
    else:
        print("Good going")
        continue
