# Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upper_lower(s):
    a = {"U": 0, "L": 0}
    for char in s:
        if char.isupper():
            a["U"] += 1
        elif char.islower():
            a["L"] += 1
        else:
            pass
    print("Original string is : ", s)
    print("No. of upper case characters : ", a["U"])
    print("No. of lower case characters : ", a["L"])

upper_lower("HELLO! This is Devanshi")
