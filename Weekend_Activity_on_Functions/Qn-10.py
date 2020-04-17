# Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

def filter(l):
    even = []
    for i in l:
        j = int(i)
        if j % 2 == 0:
            even.append(j)
    print("Even number list : ", even)
x = input("Enter comma separated list numbers between 1 to 20 : ").split(",")
filter(x)