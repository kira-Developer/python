# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------
 
 # Range 

myRange = range(1 , 100)

for number in myRange :


    print(number)


# Dictionary 

myskills = {
        'html' : '90%',
        'css' : '50%',
        'js' : '90%'
        }

for skill in myskills :
    print(skill)
    print(f'my progress in lang {skill} is : {myskills[skill]}')
