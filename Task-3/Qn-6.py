# Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

list1 = []
list2 = []
for i in range(1,31):
    if i <=  5:
        list1.append(i)
        list2.append(i*i)
    elif i >= 26:
        list1.append(i)
        list2.append(i*i)
print("Original list : ", list1)
print("list with square : ", list2)