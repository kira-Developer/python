# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os 
print(os.getcwd()) # main current working directory
print(os.path.dirname(os.path.abspath(__file__))) # directory for opened file
os.chdir(os.path.dirname(os.path.abspath(__file__))) # change current working directory
print(os.path.abspath(__file__))
file = open(r"C:\Users\kira\Desktop\python\abdullh.txt")

