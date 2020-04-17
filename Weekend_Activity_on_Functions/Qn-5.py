# Write a program that accepts a sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Sample input:
    # Hello world
    # Practice makes perfect
# Expected Output:
    # HELLO WORLD
    # PRACTICE MAKES PERFECT

n = 2
lines = ""
print("Enter strings below")
for i in range(n):
    lines += input() + '\n'
print(lines.upper())
