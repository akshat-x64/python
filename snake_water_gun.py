import random
user_input = int(input("Enter a number between 0 and 2:"))
random_1 = [0, 1, 2]
computer_input = int(random.choice(random_1))
print(computer_input)
# 0 stone
# 1 paper
# 2 sizzer
# user            computer
# 0              1
# 0               2
# 1               2
# 1               0

# computer          user
# 0                   1
# 0                   2
# 1                   2
# 1                   0


if (user_input == 0 and computer_input == 1):
    print("computer wins")

if (user_input == 2 and computer_input == 0):
    print("computer wins")

if (user_input == 1 and computer_input == 2):
    print("computer wins")
elif (user_input == 0 and computer_input == 2):
    print("user wins")
if (user_input == 1 and computer_input == 2):
    print("user wins")
elif (user_input == 1 and computer_input == 0):
    print("user wins")


elif (user_input == computer_input):
    print("game draw")
# elif (user_input == 1 and computer_input == 1):
#     print("game draw")
# elif (user_input == 2 and computer_input == 2):
#     print("game draw")
