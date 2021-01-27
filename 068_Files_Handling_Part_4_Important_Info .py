# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myfile = open('abdullh.txt' , 'r')

# myfile.truncate(6)



# print(myfile.tell())

myfile.seek(3)

print(myfile.read())

os.remove('kira.txt')
