# Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

user = input("Enter string with digits in it")
a,d = 0,0
for i in range(len(user)):
    if(user[i].isalpha()):
        a = a + 1
    else:
        d = d + 1

print("letters :", a, "\ndigits :", d)
