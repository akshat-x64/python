f = open("file4.txt", 'r')
print(type(f))
# seek function will read line from 10 position

f.seek(10)
# tell position from where it will seek
print(f.tell())
print(f.read(5))
