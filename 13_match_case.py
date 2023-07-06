# match case is same as switch case but we can a advance version of it
# in match case we don't have to write break statement


num1 = int(input("Enter number between 1 to 10:"))
match num1:
    case 1:
        print("This is correct number")
    case 2:
        print("This is correct number")
    case 3:
        print("This is correct number")
    case 4:
        print("This is correct number")
    case 5:
        print("This is correct number")
    case 6:
        print("This is correct number")
    case 7:
        print("This is correct number")
    case 8:
        print("This is correct number")
    case 9:
        print("This is correct number")
    case 10:
        print("This is correct number")
    case _ if (num1 > 10):
        print("Enter correct number")
