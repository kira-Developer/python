# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------


x = [1 ,2 , 3 ,4]
if all(x) :
    print('all elemants is true')

else:
    print('theres at least one element false')


z = [1 , 2 , 3 , 4 , []]

if any(z) :
    print('there\'s at least one element is true')

else:
    print('theres on any true elements')


print(bin(199))

a = 1
b = 2

print(id(a))
print(id(b))