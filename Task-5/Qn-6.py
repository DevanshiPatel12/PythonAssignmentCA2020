# Read any file using Python File handling concept and
# return only the even length string from the "doc.txt" file.

list = []
my_file = open('doc.txt', 'r')
my_str = my_file.readlines()

for i in my_str:
    string = ""
    i = i.strip('\n')
    list = i.split(" ")
    for j in list:
        if len(j) % 2 == 0 :
            string  = string + " " + j
    print(string)

my_file.close()