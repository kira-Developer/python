import sys
import  sqlite3
from PyQt5.QtWidgets import QApplication ,QWidget , QPushButton , QLineEdit ,QMessageBox , QLabel

a = QApplication(sys.argv)

# set main window
window = QWidget()

# messagebox
messageBox = QMessageBox.question(window , 'welcome' , 'you like Qt?' , QMessageBox.Cancel|QMessageBox.Yes)

# label
label = QLabel('username' , window )
print(label.text())
label.setText('hello user')
if messageBox == QMessageBox.Yes :
  pass
else:
  exit()

# window title
window.setWindowTitle("hello world")
window.setGeometry(500 , 500 , 500 , 500)

lineEdit = QLineEdit(window)

def get_text():
  text = lineEdit.text()
  print(type(text))
  print(text)
  lineEdit.setText('')


lineEdit.setGeometry(10 , 20 , 150 ,20)

button = QPushButton('send' , window)
button.setGeometry(10 ,50 , 100 , 20)
button.clicked.connect(get_text)

window.show()
sys.exit(a.exec_())
