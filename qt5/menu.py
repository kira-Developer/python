import sys
from PyQt5.QtWidgets import  QApplication , QMainWindow , QAction
app = QApplication(sys.argv)
window = QMainWindow()

window.setWindowTitle('menu')
menubar1 = window.menuBar()
d1 = menubar1.addMenu('file')
d2 = menubar1.addMenu('edit')
item = QAction('new' ,window)
item.setShortcut("ctrl+a")
def say_hello():
  print("hello")
item.triggered.connect(say_hello)
d1.addAction(item)

window.setGeometry(50 ,100 ,500,300 )

window.show()
sys.exit(app.exec_())