# Write a program in Python to  multiple the element of list by itself using a traditional function
# and pass the function to map to complete the operation.

l1 = []
def fun(l):
    for i in l:
        j = i*i
        l1.append(j)
    return l1
final = list(map(lambda x:x), fun([1,2,3,4]))
print(final)