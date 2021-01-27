# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime

birthday   = datetime.datetime(2003 ,3 ,25)

print(birthday)
print(birthday.strftime('%a'))
print(birthday.strftime('%A'))
print(birthday.strftime('%b'))
print(birthday.strftime('%B'))

print('#' * 50)

print(birthday.strftime('%d %B %Y'))
print(birthday.strftime('%d/%B/%Y'))
print(birthday.strftime('%d - %B - %Y'))
print(birthday.strftime('%B - %Y'))