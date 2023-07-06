# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.
def fun_1():
    try:
        li_1 = [1, 2, 3, 4, 5]
        num_1 = int(input("Enter the value of:"))
        print(li_1[num_1])
        return 1

    except:
        print("This is totally fine")
        return 0

    finally:
        print("This will executed at any cost")


aa = fun_1()
print(aa)
