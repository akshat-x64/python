def my_generators():
    for i in range(500):
        yield i


aa = my_generators()
for i in aa:
    print(i+1)