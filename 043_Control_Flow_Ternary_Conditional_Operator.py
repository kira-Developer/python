# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = 'ksa'

if country == 'ksa': print(f'the Weather in {country} is 40')
movieRate = 20

age = 19
if age < movieRate:
    print('Movie s not good 4u')

else : 
    print('move s good 4u and happy watching')


print('movie s not good 4u' if age < movieRate else 'movie s good 4u happy watching')