# Write a program that accepts a hyphen-separated sequence of words as input and
# prints the words in a hyphen-separated sequence after sorting them alphabetically.

s = input("Enter hyphen-separated string : ").split("-")
s.sort()
new_string = '-'.join(s)
print("Alphabetically sorted string : ", new_string)