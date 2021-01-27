# ----------------
# -- User Input --
# ----------------

fName = input('what\'s is your first name :')

mName = input('what\'s is your middle name :')
lName = input('what\'s is your last  name :')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()


print(f"Hello {fName} {mName:.1s} {lName}") 