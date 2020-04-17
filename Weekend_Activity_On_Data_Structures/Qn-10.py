# Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
    # Ask user to enter the number in the range of 1,50 and make sure
    # if the entered number is even append it to the even_list
    # and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

even = []
odd = []

a = input("Enter any number between 1 to 50 with comma : ").split(",")
for i in a:
    x = int(i)
    if x % 2 == 0 and len(even) < 5:
        even.append(x)
    elif x % 2 != 0 and len(odd) < 5:
        odd.append(x)

print("Even list : ", even)
print("Odd list : ", odd)
print("sum of even list element : ", sum(even))
print("sum of odd list element : ", sum(odd))
print("max of odd/even list : ", max(even+odd))
