# Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

list_1 = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for i in list_1:
    if i % 2 == 0:
        list_1.remove(i)
        new_list.append(i)
print("Updated new list : ", list_1)
print("Removed element list : ", new_list)