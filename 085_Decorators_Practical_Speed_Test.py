# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------
from time import time
def decorator(func) :
    def nestedfunc(*numbers) :
        for number in numbers :
            if number < 0:
               print('beware one of the numbers is less than zero')
               func(*numbers)
    return nestedfunc

@decorator
def calculate(n1 , n2 , n3 , n4):
    print(n1 + n2 + n3 + n4)

calculate(-5, 90, 50, 150)

print('#' * 50)

def speedtest(func) :
    def wrapper():
         start = time()
         func()
         end = time()
         print(f'function running  time is :{end - start}')
    return wrapper

@speedtest
def bigloop() :
    for number in range(1 , 2000) :
        print(number)

bigloop()

