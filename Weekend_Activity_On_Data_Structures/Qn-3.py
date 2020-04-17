# Create a list of given structure and run
    # x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
    # Access list [1, 2, 3, 4]
    # Access list [600,  700]
    # Access list [100, 300, 500, 600, 800]
    # Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
    # Access list [10]
    # Access list [ ]

x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print("task-1 : ", x[5][0:4])
print("task-2 : ", x[6:8])
y = [x[i] for i in range(len(x)) if i % 2 == 0]
print("task 3 : ", y)
x.reverse()
print("task-4 : ", x)
x.reverse()
print("task-5 : ", [x[5][5][0]])
x.clear()
print("task-6 : ", x)
