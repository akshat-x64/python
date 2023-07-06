# # Function to double the input
# def double(x):
#   return x * 2
# # Lambda function to double the input
# lambda x: x * 2


# # Function to calculate the product of two numbers
# def multiply(x, y):
#     return x * y
# # Lambda function to calculate the product of two numbers
# lambda x, y: x * y

# lambda x, y: print(f'{x} * {y} = {x * y}')

# double_1 = lambda x:x*2

def aa(xx, y):
    return xx(4)*y


# print(aa(double_1, 2))
print(aa(lambda x: x*2, 2))
