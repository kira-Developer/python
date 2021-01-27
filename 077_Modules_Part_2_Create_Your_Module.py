# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------



import module
print(dir(module))

module.sayHello('kira')
module.sayHello('abdullh')
module.sayHello('ner')
print('#' * 50)

import module as test

test.sayHello('abdullh')

print('#' * 50)

from module import sum

sum(100 , 22)