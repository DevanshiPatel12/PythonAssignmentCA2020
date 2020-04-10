# Write a program in Python to find out the character in a string which is uppercase using list comprehension.

user = input("Enter string : ")
list1 = [i for i in user if i.isupper() and i.isalpha()]
print("List : ",list1)
