# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 17 
country = 'ksa'

print(age > 16)
print(country == 'ksa')

print(age > 16 and country == 'ksa')
print(age > 16 and country == 'egypt')

print('=' * 50)

print(age > 16 or country == 'ksa')
print(age > 16 or country == 'egypt')
print(age > 20 or country == 'egypt')

print('=' * 50)


print(age > 16)
print(not age > 20)
