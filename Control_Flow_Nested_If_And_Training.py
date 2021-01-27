# ---------------
# -- Nested If --
# ---------------

uName = 'abdullh'
cName = 'php course'
cprice = 100
cdiscount = 12
country = 'ksa'
isstudent = 'yes'
if country == 'egypt' or country == 'ksa':

    if isstudent == 'yes':

        print(f'hello {uName} the course "{cName}" price is: {cprice - 60}')
    else:
        print(f'hello {uName} the course "{cName}" price is: {cprice - 13}')

elif country == 'kuwait':
    print(f'hello {uName} the course "{cName}" price is: {cprice - 30}')


else:
    print(f'hello {uName} the course "{cName}" price is : {cprice - cdiscount}')
