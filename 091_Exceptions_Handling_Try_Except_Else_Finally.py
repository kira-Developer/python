# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

# number = int(input('write your age:'))
# print(number)
# print(type(number))

try : # try the code and test errors
    number = int(input('write your age :'))
except ValueError : # handle the error if its found
    print('this is not integer')


else : # if theres no errors
    print(number)
finally :
    print('thank you')