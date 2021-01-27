# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------
myskill = {
    'html': '60%',
    'python': '40%',
    'php': '40%'
}


def show_skills(name, *skills, **skillwithprogress):
    print(f'Hello {name}\nskills without progress it\'s :')
    for skill in skills:
        print(f'-{skill}')

    for skill_key, skill_value in skillwithprogress.items():
        print(f'{skill_key} => {skill_value}')


show_skills('kira', 'html', 'css', 'js', **myskill)
