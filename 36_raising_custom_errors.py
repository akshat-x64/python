
# a = int(input("Enter a number:"))
# if (a < 5 or a > 9):
#     raise ValueError("This should be between 5 or 9 or should be 5 or 9 ")


b = input("type quit:")
a = b.lower()
if (a == "quit"):
    pass
else:
    raise ValueError("Please 'quit only'")
