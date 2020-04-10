# more about Yield, next, generator

def simple_Generator():
    yield 1
    yield 2
    yield 3

# x is a generator object
x = simple_Generator()

# Iterating over the generator object using next
print(x.__next__())
print(x.__next__())
print(x.__next__())