# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
    'name': 'abdullh'

}

print(user)

user.clear()
print(user)
print('=' * 50)

# update()
member = {
    'name': 'abdullh'
}

print(member)
member['age'] = 17
print(member)
member.update({'username': 'kira'})
print(member)

print('=' * 50)

# copy()

main = {

    'name': 'abdullh'
}

print(main)

b = main.copy()
print(b)
main['skills'] = 'Fighting'

print(main)
print(b)

print('=' * 50)

# keys() + values()
print(main.keys())
print(main.values())
