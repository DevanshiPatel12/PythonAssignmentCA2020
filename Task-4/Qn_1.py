# Write a program in Python find the values which is not divisible 3 but is should be a multiple of 7.
# Make sure to use only higher order function. """

def n_list(l):
    new = list(filter(lambda x: x%3 != 0 and x%7 == 0, 1))
    print(new)