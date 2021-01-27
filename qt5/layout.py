import sys
from PyQt5.QtWidgets import QApplication , QWidget , QVBoxLayout , QPushButton

app = QApplication(sys.argv)

window = QWidget()
lay = QVBoxLayout()

for btn in range(5):
  btn = QPushButton('hi', window)
  lay.addWidget(btn)
window.setGeometry(100 , 100 , 500 ,500)
window.setLayout(lay)
window.show()
sys.exit(app.exec_())