# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------

list1 = [1,2,3,4,5]
list2 = ['a' ,'b']
tuple1 = ('man' , 'woman' , 'girl' , 'boy')
dict1 = {'name' : 'abdullh', 'age' : 17 , 'country' : 'ksa'}

ultimatelist = zip(list1 , list2)

for item in ultimatelist :
    print(item)

print('#' * 50)

for item1 , item2 , item3 , item4  in zip(list1 , list2 , tuple1 , dict1) :
    print(item1 , item2 , item3 , item4 , dict1[item4])
