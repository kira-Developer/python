# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------
# Use Map With Predefined Function

def formatText(text) :
    return f'- {text.strip().capitalize()} -'

myTexts = ['  abdullh' , 'kira' , '  ner    ']
myformated = map(formatText , myTexts)

print(myformated)

for name in myformated :
    print(name)

# for name in list(myformated):
#     print(name)
print('#' *  50)

for name in list(map(lambda text : f'- {text.strip().capitalize()} -' , myTexts)):
    print(name)