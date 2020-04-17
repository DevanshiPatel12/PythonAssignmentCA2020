# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

def s_length(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        print("Max length string is : ", s1)
    elif l2 > l1:
        print("Max length string is : ", s2)
    else:
        print("Both strings have equal length.")

s1 = input("Enter first string : ")
s2 = input("Enter second string : ")
s_length(s1,s2)