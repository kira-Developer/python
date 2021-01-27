# import Library
import sys
from PyQt5.QtWidgets import QApplication , QLabel , QPushButton ,QWidget , QLineEdit

# set app
app = QApplication(sys.argv)
window = QWidget()

# window  properties
window.setWindowTitle('my first project')
window.setGeometry(100 , 100 ,400 ,300)

# functions
def additions():
  n1 = int(line1.text())
  n2 = int(line2.text())
  value = f"result: {n1 + n2}"
  result.setText(str(value))

def subtractions():
    n1 = int(line1.text())
    n2 = int(line2.text())
    value = f"result: {n1 - n2}"
    result.setText(str(value))


def multipications():
  n1 = int(line1.text())
  n2 = int(line2.text())
  value = f"result: {n1 * n2}"
  result.setText(str(value))


def divsions():
  n1 = int(line1.text())
  n2 = int(line2.text())
  value = f"result: {n1 / n2}"

  result.setText(str(value))

# lineEdit
line1 = QLineEdit(window)
line2 = QLineEdit(window)

# lineEdit properties
line1.move(40 , 50)
line2.move(200 , 50)

# label
first_number = QLabel('number one' , window)
second_number = QLabel('number two' , window)

# lable properties
first_number.move(70 , 30)
second_number.move(230 , 30)

# button
addition  = QPushButton('+',window)
subtraction  = QPushButton('-',window)
multipication = QPushButton('*',window)
divsion = QPushButton('/',window)

# button properties
addition.setGeometry(270 , 200 , 31 ,23) , subtraction.setGeometry(210 , 200 , 31 ,23) , multipication.setGeometry(150 , 200 , 31 ,23) ,divsion.setGeometry(100 , 200 , 31 ,23)

# result
result = QLabel('result' , window)

# button properties
result.setGeometry(170 , 100 , 200 , 100)

# events
addition.clicked.connect(additions)
subtraction.clicked.connect(subtractions)
multipication.clicked.connect(multipications)
divsion.clicked.connect(divsions)

# show window
window.show()
sys.exit(app.exec_())