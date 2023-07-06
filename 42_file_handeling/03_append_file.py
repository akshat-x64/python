f = open("file2.txt", 'a')
f.write("This is a sample text\n")
f.close()


# shortcut method without all of this

with open('file2.txt', 'r') as f:
    print(f.read())
