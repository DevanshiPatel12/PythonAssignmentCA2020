# Write a program in Python to allow the error of syntax to go in exception.
# HINT: use SyntaxError

try:
    x = "Devanshi"
    a = eval("My name is " + x)
    print(a)
except SyntaxError:
    print("You have Syntax Error")
finally:
    print("Done")