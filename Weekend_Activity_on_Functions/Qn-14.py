# What is the output of the following codes:

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

# Ans. it will return 2.

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()

# Ans. it will give ‘NameError’. Name ‘f’ is not defined.
