import os
allFiles = os.listdir("Akshat")
print(allFiles)

for i in allFiles:
    print(i)
    print(os.listdir(f"Akshat/{i}"))


# to get the current directory
print(os.getcwd())
os.chdir("c:/")
print(os.getcwd())
