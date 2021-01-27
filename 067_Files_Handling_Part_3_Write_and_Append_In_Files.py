# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------


myfile = open('ceratebypython', 'w')
mylist = ['abdullh \n' , 'kira']
myfile.write('hello from python file with love \n' * 5)
myfile.write('second line\n')
myfile.writelines(mylist)

