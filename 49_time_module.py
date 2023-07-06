import time

def usingfor():
    for i in range(50001):
        print(i)

def usingWhile():
    i = 0
    while(i<50001):
        print(i)
        i = i+1


current = time.time()
# usingfor()
t1 = time.time() - current
current = time.time()
# usingfor()
t2 =  time.time() - current
print(t1,t2)


print("Akshat")
time.sleep(5)
print("Dwivedi")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t).split(" ")
print(formatted_time)