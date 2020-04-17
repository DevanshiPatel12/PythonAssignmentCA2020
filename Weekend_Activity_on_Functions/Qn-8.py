# Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20.

def n_square():
    l = []
    for i in range(1,21):
        square = i * i
        l.append(square)
    t = tuple(l)
    print(t, type(t))
n_square()