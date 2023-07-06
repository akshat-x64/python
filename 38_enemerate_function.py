marks = [2, 32, 3, 43, 3, 43, 43, 4, 34, 3, 4, 34, 34]

for index, i in enumerate(marks):
    print(i)
    if (index == 3):
        print("great Akshat")


# you can start with another number rather than 0

for j, i in enumerate(marks, start=1):
    print(i)
    if (j == 3):
        print("great Akshat")
