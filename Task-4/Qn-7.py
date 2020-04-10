# -------- Example of Decorator

def main_deco(function):
    def function_1():
        print("I am inside the function_1 and printing before the function()")
        function()
        print("I am inside the function_1 and printing after the function()")
    return function_1
def new_deco():
    print("need some decoration")

#syntax to call decorator
decoration = main_deco(new_deco)
decoration()

# -------------------------------------- other way
def main_deco(function):
    def function_1():
        print("I am inside the function_1 and printing before the function()")
        function()
        print("I am inside the function_1 and printing after the function()")
    return function_1

@main_deco
def new_deco():
    print("need some decoration")

new_deco()