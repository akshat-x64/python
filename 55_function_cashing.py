import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
print(fx(55))
print("1111111111")
print(fx(22))
print("22222222222222")
print(fx(11))
print("3333333333")


print(fx(55))
print("1111111111")
print(fx(22))
print("22222222222222")
print(fx(11))
print("3333333333")
