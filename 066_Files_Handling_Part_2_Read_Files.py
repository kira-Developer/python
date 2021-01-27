# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myfile = open('abdullh.txt')

print(myfile)
print(myfile.name)
print(myfile.mode)
print(myfile.encoding)

# print(myfile.read())

# print(myfile.readline())

# print(myfile.readlines())


for line in myfile : 

    print(line)

    if line.startswith('3') :

      break

  myfile.close()

