# -----------------
# -- Set Methods --
# -----------------

# clear()
a = {1, 2, 34, 454, 'abc'}
a.clear()

print(a)

# uinon()

b = {1, 3, 'test'}
c = {'test', 2, True}
x = {'hi', 4, 2.3}

print(b | c | x)
print(b.union(c, x))


# add()
d = {1, 3, 4}
d.add(6)

print(d)

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

# remove()
g = {1, 2, 3, 4}
g.remove(3)
print(g)


# discard()
k = {1, 2, 3, 4}
k.discard(6)
print(g)


# pop
s = {'a' , True , 2}
print(s.pop());

# update

j = {1 , 3, 5 ,6}
n = {'a' , 1 , 'c'}
j.update(n)
print(j)
