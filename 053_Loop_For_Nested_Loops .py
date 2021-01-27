# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------


peopless = ['abdullh' , 'kira' , 'ner']

skills = ['html' , 'css' 'js']

for name in peopless : # outer loop

    print(f'{name} skills is :')

    for skill in skills : # inner loop 

        print(f'- {skill}')


# dictionary 


peoples = {

        'kira' : {
            'html' : '70%',
            'css' : '80%',
            'js' : '70%'
            },
        'abdullh' : {
            'html' : '20%',
            'css' : '50%',
            'js' : '100%'
            }
        }


print(peoples['kira'])
print(peoples['abdullh'])


print(peoples['kira']['js'])
print(peoples['abdullh']['js'])


for name in peoples:

  print(f"Skills and Progress For {name} Is: ")

  for skill in peoples[name]:

        print(f"{skill.upper()} => {peoples[name][skill]}")
