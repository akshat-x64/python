f = open("file5.txt", 'w')

f.write("This is a sample txt file")
f.truncate(16)
f.close()
f = open("file5.txt", 'r')
print(f.read())
f.close()
