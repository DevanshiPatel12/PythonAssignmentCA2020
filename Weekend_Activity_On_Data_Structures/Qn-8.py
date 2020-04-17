# Write a program in Python to iterate through the string “hello my name is abcde”
# and print the string which has even length of word.

a = "hello my name is abcde"
b = a.split(" ")
for i in b:
    j = len(i)
    if j % 2 == 0:
        print("Word with even length : ", i)