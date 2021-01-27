from PyQt5.QtWidgets  import QApplication , QWidget
import sys
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

app =QApplication(sys.argv)
window = QWidget()

window.setAutoFillBackground(True)

p = window.palette()
p.setColor(window.backgroundRole() , Qt.red)

window.setPalette(p)
window.show()
sys.exit(app.exec_())