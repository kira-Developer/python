# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re

my_str = re.search(r'[A-Z]', 'Abdullh')
print(my_str)
print(my_str.span())
print(my_str.string)
print(my_str.group())

print('#' * 50)
is_email = re.search(r'[A-z0-9\.]+@[A-z0-9]+\.(com|net)' , 'ab@mkka.com')

if is_email :
    print('this is  a valid email')
    print(is_email.span())
    print(is_email.string)
    print(is_email.group())

else :
    print('this is not a valid email')

print('#' * 50)
email_input = input('please write your email: ')
search  = re.findall(r'[A-z0-9\.]+@[A-z0-9]+\.com|net' , email_input)

empty_list = []

if search != [] :
    empty_list.append(search)
    print('emaill added')

else :
    print('invalid email')

for email in empty_list :
    print(email)