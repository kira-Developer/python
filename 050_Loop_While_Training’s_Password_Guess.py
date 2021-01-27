# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

mainPassword = "abdullh@123"

inputPassword = input('enter your password:')

tries = 4 

while inputPassword != mainPassword :

    tries -= 1
    print(f"wrong password , {'the last tries' if tries == 0 else tries} chance left")
    inputPassword = input('enter your password:')

    if tries == 0 : 
        print('can\'t add password anymore')
        break

else : 
    print('the password is true')



