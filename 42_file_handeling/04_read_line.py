f = open("file2.txt", 'r')
while True:
    line = f.readline()
    print(line)
    if (not line):
        break
f.close()
g = open("file3.txt")
while True:
    line = g.readline()
    if (not line):
        break
    f1 = line.split(",")[0]

    f2 = line.split(",")[1]
    f3 = line.split(",")[2]
    print(f"These are the words {f1} {f2} {f3}")
