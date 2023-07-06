# read mode is defalut mode if we don't write then also it will work
f = open('file.txt', 'r')
print(f)

text = f.read()
print(text)
f.close()

# we can real file using 'rb' for binary and "rt" for reading text file

f = open('file.txt', 'rb')
print(f.read())


f = open('file.txt', 'rt')
print(f.read())
f.close()
