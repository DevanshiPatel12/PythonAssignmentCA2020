# Write a program to handle an error if the user entered the number more than four digits
# it should return “Please length is too short/long !!! Please provide only four digits”

try:
    number = input("Enter the number : ")
    if len(number) <= 4:
        print("Perfect")
    else:
        raise Exception
except Exception:
    print("Length is too short/long! Please provide only four digits")