# Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def addition():
    a, b = input("Enter two numbers with comma : ").split(",")
    print(type(a),type(b))
    sum = int(a) + int(b)
    print("Sum : ", sum)

addition()