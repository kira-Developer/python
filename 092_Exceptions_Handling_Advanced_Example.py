# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------


the_file = None
the_tries = 3

while the_tries > 0 :
    try:
        print('enter the file name absolute path to open')
        print(f'you have {the_tries} tries left')
        print(r'example : C:\Users\kira\Desktop\python')
        file_name = input('file name => :').strip()
        the_file = open(file_name)
        print(the_file.read())
        break


    except FileNotFoundError :
             print('file not found please be sure the name is valid')
             the_tries -= 1

    finally:
         if the_file is not None :
               the_file.close()
         print('file close')

else :
    print('all tries is done')
