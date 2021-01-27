# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

def show_skills(*skills):

     print(type(skills))

     for skill in skills:

         print(f'{skill}')

show_skills('html' , 'css' , 'js')

print('=' * 50)

def show_skills(**skills):
    print(type(skills))
    
    for skill , value in skills.items():
        print(f'{skill} => {value}')

show_skills(html = '80%' , js = '50%', python = '20%')
