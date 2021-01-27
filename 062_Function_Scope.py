# --------------------
# -- Function Scope --
# --------------------

x = 1  # global Scope

def one():
    global x
    x = 2
    print(f'print variable from function scope {x}')
def two():
    x = 4
    print(f'print variable form function scope {x}')
print(f'print variable from global scope {x}')
one()
two()
print(f'print variable from global scope after one function is call {x}')