# ----------------------
# -- Type Conversion --
# ----------------------
# str()
a = 10

print(type(a))
print(type(str(a)))


print('=' * 50)
c = 'abdullh'
d = [1, 2, 3, 4]
e = {'A',  "B", "C"}
f = {'A': 1, 'B': 2}

# tuple()

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

print('=' * 50)

# list

g = 'abdullh'
h = (1, 2, 3, 4)
i = {'A',  "B", "C"}
l = {'A': 1, 'B': 2}
print(list(g))
print(list(h))
print(list(l))
print(list(i))


print('=' * 50)

z = 'abdullh'
v = (1, 2, 3, 4)
m = ['A',  "B", "C"]
o = {'A': 1, 'B': 2}

# set()
print(set(z))
print(set(v))
print(set(m))
print(set(o))


print('=' * 50)


k = (('a', 1), ('b', 2), ('c', 3))
u = [['a', 1], ['b', 2], ['c', 3]]


# dict()

print(dict(k))
print(dict(u))
