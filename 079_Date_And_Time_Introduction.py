# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# print the currnet date and time

print(datetime.datetime.now())

print('#' * 50)

# print the current date year
print(datetime.datetime.now().year)

# print the current date month
print(datetime.datetime.now().month)

# print the current day
print(datetime.datetime.now().day)

print('#' * 50)

# print start and end of date

print(datetime.datetime.min)
print(datetime.datetime.max)


print('#' * 50)

# print the current time

print(datetime.datetime.now().time())

print('#' * 50)

# print the current time hour
print(datetime.datetime.now().time().hour)

# print the current time minute
print(datetime.datetime.now().time().minute)

# print the current time second
print(datetime.datetime.now().time().second)

print('#' * 50)

# print start and end of time
print(datetime.time.min)
print(datetime.time.max)

# print specific date
print(datetime.datetime(2003 , 3 , 25))
print(datetime.datetime(2003 , 3 , 25 , 7 , 40 , 33 , 132413))

print('#' * 50)

# how many day i'm lived

birthday = datetime.datetime(2003 , 3 , 25)
date = datetime.datetime.now()
print((date - birthday).days)