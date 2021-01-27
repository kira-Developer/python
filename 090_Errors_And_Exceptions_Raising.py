# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------

x = -10
y = 'abdullh'
if x < 0 :
     print(f'the number {x} is less than  zero')
     raise Exception(f'the number {x} is less than zero')
     print('this will not print decause the error')

else :
    print(f'{x} is good number and ok')

print('print message after if condition')
print('#' * 50)

if type(y) != int :

    raise ValueError('only number')