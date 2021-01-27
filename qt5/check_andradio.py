import sys
from PyQt5.QtWidgets import QApplication , QWidget , QPushButton , QRadioButton , QCheckBox

app = QApplication(sys.argv)

window = QWidget()
r1 = QRadioButton('male' ,window)
r2 = QRadioButton('female' , window)
r1.move(200 , 200)
r2.move(100 , 200)

window.setGeometry(100 , 100 , 500 ,500)

window.show()
sys.exit(app.exec_())