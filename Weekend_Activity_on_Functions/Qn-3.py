# Create a function that takes a list and returns a new list with unique elements of the first list.

def unique(l):
    u_list = []
    for i in l:
        if i not in u_list:
            u_list.append(i)
    print("original list : ", l)
    print("Unique list: ", u_list)

unique([1,2,2,2,3,4,5,5,"a","a",1.5,1.5])