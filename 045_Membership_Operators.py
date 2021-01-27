# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

 # string 


name = 'abdullh'

print('s' in name) 
print('a' in name) 

print('#' * 50)


# list 

lang = ['php', 'js' , 'python']
print('php' in lang)
print('html' in lang)
print('python' not in lang)
print('css' not in lang)

print("#" * 50)


countriesOne = ['egypt' , 'ksa' , 'kuwait' , 'bahrain']

countrieOnesdiscount = 80 


countriesTwo = ['ltaly' , 'usa' ]
countriesTwodiscount = 50

mycountry = 'ksa'

if mycountry in countriesOne :
    print(f'your discount is {countrieOnesdiscount}')

elif mycountry in countriesTwo :
    print(f'your discount is {countriesTwodiscount}')
