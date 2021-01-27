# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

User = {
    "name" : 'abdullh' ,
    'age' : 17 ,
    'cuntry': 'ksa'
}
print(User)
print(User['name'])
print(User.get('age'))

print('=' * 50);

print(User.keys())
print(User.values())
print('=' * 50);
# Two-Dimensional Dictionary
mylang = {
    'one': {
        'lang' : 'html' ,
        'progrees' : '90%'
    } ,
    'two' : {
        'lang' : 'js' ,
        'progrees' :"60%"
    }
}

print(mylang)
print(mylang['one']['lang'])

print('=' * 50);

print(len(mylang))
print(len(mylang['two']))


print('=' * 50);


# Create Dictionary From Variables

frameworkOne = {
  "name": "laravel",
  "progress": "80%"
}

frameworkTwo = {
  "name": "bootstrip",
  "progress": "80%"
}

frameworkThree = {
  "name": "node js",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree

}

print(allFramework)
