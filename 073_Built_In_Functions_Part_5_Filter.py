# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def checkNumber(num) :

        return  num < 10

mynumbers = [1 , 3 , 5 , 21 , 32 ,10]

myresult = filter(checkNumber , mynumbers)

for number in myresult :
    print(number)


print('#' * 50)

# Example 2


def checkName(name):

    return name.startswith('k')

myNames = ['abdullh'  , 'kira' , 'ksa' , 'bander']

myNameResult = filter(checkName , myNames)

for name in myNameResult :
    print(name)

print("#" * 50)

myNames = ['abdullh'  , 'kira' , 'ksa' , 'bander']

for p in filter(lambda name : name.startswith('a') , myNames):
    print(p)