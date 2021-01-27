# ------------------------
# -- Dictionary Methods --
# ------------------------


# setdefault()

user = {
    'name' : 'abdullh'
}
print(user)
print(user.setdefault('age' , 17))
print(user)

print('=' * 40)

# popitem()

member = {
    'Name' : 'abdullh' ,
    'Skill' : 'PS4'
}
print(member)
member.update({'age' : 17})
print(member.popitem())

print('=' * 40)

# items()

view = {
      'Name' : 'abdullh' ,
    'Skill' : 'PS4'
}

allItems = view.items()
print(view)
view['age'] = 17
print(view)

print('=' * 40)

# fromkeys()

a = ('oneKey'  , 'twoKey' , 'trheeKey')
b = 'x'
print(dict.fromkeys(a , b))