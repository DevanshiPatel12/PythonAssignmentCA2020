# https://www.programiz.com/python-programming/exception-handling
# Go through this link to understand Finally and Raise concept.

try:
    x = int(input("Enter any number : "))
    if x >= 0 and x % 2 == 0:
        print("Number is even")
    elif x >= 0 and x % 2 != 0:
        print("Number is odd")
    else:
        raise Exception
except Exception:
    print("Negative number.")
finally:
    if x < 0:
        print("Sorry !!")
    else:
        print("Square is : ", x*x)
