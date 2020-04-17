# Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

def reverse_string(s):
    s1 = s[::-1]
    print("Reverse string is : ", s1)
    print(type(s1))
reverse_string("1234abcd")
