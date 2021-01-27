
# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------


def decorator(func) : # decorsror

    def nestedfunc() : # any name its just for decoration

        print('before') # message from decorator
        func() # excute function
        print('after')

    return nestedfunc # reutrn all date

@decorator
def sayhello() :
    print('hello from say hello function')
sayhello()

