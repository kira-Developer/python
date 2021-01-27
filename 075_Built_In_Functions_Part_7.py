# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)


mySkills = ["Html", "Css", "Js", "PHP"]
myskillWithCounter = enumerate(mySkills , 20)
print(type(myskillWithCounter))
for  counter , skill in myskillWithCounter:
    print(f'{counter} - {skill}')

print('#' * 50)
# help()
print(help(print))

print('#'  * 50)

# reversed(iterable)

name = 'abdullh'

print(reversed(name))

for letter in reversed(name) :
    print(letter)

print('#' * 50)
list = [1 , 3 , 5 , 6]

for number in reversed(list):

    print(number)