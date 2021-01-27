# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------


uName = 'abdullh'
cName = 'php course'
cprice = 100 
cdiscount = 12
country = 'ksa'
if country == 'egypt':
    print(f'hello {uName} the course "{cName}" price is: {cprice - 13}')
elif country == 'ksa':
    print(f'hello {uName} the course "{cName}" price is: {cprice - 30}')


else:
    print(f'hello {uName} the course "{cName}" price is : {cprice - cdiscount}')
