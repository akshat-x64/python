num1 = int(input("Enter a number for num1"))
num2 = int(input("Enter a number for num2"))
num3 = int(input("Enter a number for num3"))

if (num1 > num2):
    if (num1 > num3):
        print(num1, "is greatest")
elif (num2 > num3):
    print(num2, "is greatest")
else:
    print(num3, "is greatest")
