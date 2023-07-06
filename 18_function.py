def isPrime(num):
    num1 = 2
    while (num1 < num):
        if (num % num1 == 0):
            print(num, "is not prime")

        num1 = num1+1
    print(num, "is prime")


isPrime(11)
isPrime(9)
isPrime(5)
isPrime(2)


# if you want to remain a function empty we can use #pass function
def isNumber():
    pass
# if we write pass we dont get any error
