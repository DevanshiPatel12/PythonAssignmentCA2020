# What is the output of the following code examples?

x=123
for i in x:
    print(i)

# Ans. TypeError: ‘int’ object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("Error")

# Ans. it will print 0 Error 1 Error 2.

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Ans. It will print 0 1 2 3 4 and after that it will break the loop
