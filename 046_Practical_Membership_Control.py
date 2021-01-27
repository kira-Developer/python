# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins

admins = ['adbullh', 'kira', 'L']
# Login

name = input('please type your name ').strip()

# If Name is In Admin

if name in admins:
    print(f'hello {name} welcome back')
    option = input('delete or update your name ?').strip()
 # Update Option

    if option == 'update':
     theNewName = input('your new name please').strip()
     admins[admins.index(name)] = theNewName
     print('Name update')
     print(admins)

# Delete Option

    elif option == 'delete':
          admins.remove(name)
          print('name is deleted')
          print(admins)

# Wrong Option
    else :
     print('woring option')

else:
    print('you are not an admin')
