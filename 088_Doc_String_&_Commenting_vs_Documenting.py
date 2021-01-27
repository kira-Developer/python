# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------

def abdullh(name):
    '''this is function to say hello from abdullh'''
    print(f'hello {name} from abdullh')

print(abdullh.__doc__)
print('#' * 50)
help(abdullh)