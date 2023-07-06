def numFact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * numFact(n-1)


print(numFact(3))
print(numFact(4))
print(numFact(5))
