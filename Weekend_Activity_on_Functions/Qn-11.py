# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#             Use filter() to filter elements of a list
#             Use lambda to define anonymous functions

def n_list(l):
    even = list(filter(lambda x : x % 2 == 0, l))
    print("Even list : ", even)
    square = list(map(lambda x: x*x, even))
    print("Suare of list : ", square)

n_list([1,2,3,4,5,6,7,8,9,10])