def revNumber(num):
    '''This is to inform you that this function reverse a number '''
    rev_Number = 0
    while (num != 0):
        temp = num % 10
        rev_Number = (rev_Number*10)+temp
        num = num//10

    return rev_Number


print(revNumber(234233))
print(revNumber(54334))
print(revNumber(54353))
print(revNumber.__doc__)
