# defaults arguments

def findAvg(a=6, b=2):
    print((a+b)/2)


findAvg(4, 5)
findAvg(b=10)
findAvg(4)


# keyword arguments


findAvg(b=10, a=6)


# required agruments
def compareNumber(a, b):
    if (a > b):
        print("a is greater")

    else:
        print("b is greater")


# in this situation arguments are required any how
compareNumber(5, 3)
# compareNumber(5)
compareNumber(3, 5)


# taking tuple as arguments

def allAvg(*numbers):
    sum = 0
    for i in numbers:
        sum += i

    print("The avg of all number is ", sum/len(numbers))


allAvg(4, 5, 6, 4, 3, 4, 4)


def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")


# variable length arguments
def addAllNum(*numAll):
    numFinal = 0
    for i in numAll:
        numFinal = numFinal+i
    print(numFinal)


addAllNum(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
