# Write a program which accepts a sequence of comma-separated numbers from the console and generate a list
# and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

l = input("Enter comma separated numbers : ").split(",")
t = tuple(l)
print(l, type(l))
print(t, type(t))
