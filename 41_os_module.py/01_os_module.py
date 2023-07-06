import os


if (not os.path.exists("Akshat")):
    os.mkdir("Akshat")


for i in range(1, 101):
    os.mkdir(f"Akshat/Day{i}")
