# Write a program to find out the occurrence of a specific word from an alphanumeric statement.
# Example: 12abcbacbaba344ab
# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

s = '12abcbacbaba344ab'
dict = {}
for char in s:
    if char.isalpha():
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
print(dict)