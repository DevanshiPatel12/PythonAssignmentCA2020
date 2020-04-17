# Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

list_1 = [[1,3,5,7,9,10],[2,4,6,8]]
new_list = []
for l in list_1:
    for i in l:
        if i != 0:
            new_list.append(i)

print("nested list : ", list_1)
print("combined list : ", new_list)