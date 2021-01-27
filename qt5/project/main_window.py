# import libraries
import sys
import os
from PyQt5.QtWidgets import QApplication ,QWidget , QPushButton , QLineEdit , QLabel
from PyQt5.QtGui import  QPixmap
sys.path.append(r'C:\Users\kira\Desktop\python\qt5\project\database_inforamation')
print(sys.path)

# set app
app = QApplication(sys.argv)
# main window
main_window = QWidget()
main_window.setGeometry(100 , 100 , 428 , 322)
main_window.setWindowTitle('login')
# the background
backGroound = QLabel(main_window)
imge = QPixmap('imgs/gradient-geometric-shape-background_78532-374.jpg')
backGroound.setPixmap(imge)
# the lable
lableUser = QLabel('username' , main_window)
lablePassword = QLabel('password' , main_window)

lableUser.move(100 , 50)
lablePassword.move(100, 80)

# line edit
lineEditUsername = QLineEdit(main_window)
lineEditPassword = QLineEdit(main_window)

lineEditUsername.move(200 , 50)
lineEditPassword.move(200 , 75)

# button
singIn = QPushButton('sign in' , main_window)
singUp = QPushButton('sign up' , main_window)

singIn.move(150 , 110)
singUp.move(250 , 110)
# function
def singin():

  db = database().check_user(lineEditUsername.text() , lineEditPassword.text())
  if db == 0 :
    print('login')
  elif db == 1 :
    print('the pass is not found')
  else: print('user not found')

  print(db)

# evint
singIn.clicked.connect(singin)





main_window.show()
sys.exit(app.exec_())