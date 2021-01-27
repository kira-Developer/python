# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

name = 'abdullh'
mylist = [1 ,3,4 ,5]

for str  in name :
    print(str)

print('#' * 50)

for number in mylist :
    print(number)

print('#' * 50)
iter = iter(name)

print(next(iter)) ; print(next(iter)) ; print(next(iter)) ; print(next(iter)) ; print(next(iter)) ; print(next(iter)) ; print(next(iter))

