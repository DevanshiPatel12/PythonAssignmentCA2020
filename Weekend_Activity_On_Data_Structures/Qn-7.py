# Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.

a = input("Enter string : ")
b = a[::-1]
print("Reverse string : ", b)
vowels = 'aeiou'
for x in a:
    for v in vowels:
        if v == x:
            print("Vowel : ", v, ", Index : ", a.index(v))