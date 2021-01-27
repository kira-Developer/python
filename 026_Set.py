# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed


mysetOne = {"osama", 'ahmed', 100, True, False}

print(mysetOne)


mysetTow = {1, 2, 3}
# print(mysetTow[0:2])

# mysetThree = {'abdullh', 100, 100.5, True, [1, 2, 3]} # TypeError: unhashable type: 'list'
mysetThree = {'abdullh', 100, 100.5, True, (1, 2, 3)}


print(mysetThree)


# Items Is Unique

mysetFour = {1, 3, 'abc', 'abc', 1}

print(mysetFour)
