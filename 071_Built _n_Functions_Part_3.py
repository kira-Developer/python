# ------------------------
# -- Built In Functions --
# ------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------


# abs()

print(abs(100))
print(abs(-100))
print(abs(10.20))
print(abs(-19.23))

print('#'  * 60)

# pow(base, exp, mod) => Power

print(pow(10 , 10 ))  # 10 ** 10
# print(10**10)
print(pow(2 , 5 , 10))


print('#' * 60)


# min(item, item , item, or iterator)
list = [1 , 4  , -4 , 20]
num = (1 , 3 , 45)
print(min(1 , 10 , -50 , 20 ,30))
print(min('a' , 'b' , 'x' ,'abdullh'))
print(min(num))
print(min(list))

print('#' * 60)

# max(item, item , item, or iterator)

print(max(2 , 4 , 5 , 6))
print(max(list))
print(max(num))
print(max('a' , 'b' , 'c'))

print('#'  * 60 )

# slice(start, end, step)
a = ['a' , 'b' , 'c' , 'd']

print(a[:3])
print(a[slice(2 , 3)])

