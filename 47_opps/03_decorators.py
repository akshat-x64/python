def greet(aa):
    def aa1(*args, **kwargs):
        print("Function will now execute")
        aa(*args, **kwargs)
        print("Thanks for executing this function")
    return aa1


@greet
def print_yes():
    print("Hello world")


print_yes()


@greet
def add(a, b):
    print(a+b)


add(1, 2)

# Python Decorators

# Python decorators are a powerful and versatile tool that allow you
# to modify the behavior of functions and methods. They are a way to
# extend the functionality of a function or method without modifying
# its source code.

# A decorator is a function that takes another function as an argument
# ‘and returns a new function that modifies the behavior of the original
# function. The new function is often referred to as a "decorated"
# function. Thepbasic syntax for using a decorator is the following:
