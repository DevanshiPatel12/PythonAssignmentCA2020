# Write a function to compute 5/0 and use try/except to catch the exceptions

try:
    a = 5/0
except ZeroDivisionError:
    print("You divided number with zero. Error!")