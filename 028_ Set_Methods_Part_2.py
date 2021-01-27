# -----------------
# -- Set Methods --
# -----------------


# difference()

a = {1, 2, 3, 4}
b = {1, 2, 'abc', True}
print(a)
print(a.difference(b)) # a - b


print("=" * 40)

# difference_update()


c = {1, 2, 3, 4}
d = {1, 2, 'abc', True}
print(c)
c.difference_update(d) # a - b
print(c)

print("=" * 40)


# intersectoin()

e = {1, 2, 3, 'X'}
f = {'abc', 'X', 2}
print(e)
print(e.intersection(f)) # e & f
print(e)

print("=" * 40)


# intersectoin_update()

g = {1, 2, 3, 'X'}
h = {'abc', 'X', 2}
print(g)
g.intersection_update(h) # g & h
print(g)


print("=" * 40)


# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"abc", "kira", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)

print("=" * 40)  # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"abc", "kira", 1, 2, 4, "X"}
print(k)
k.symmetric_difference_update(l)  # k ^ l
print(k)


