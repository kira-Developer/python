from PyQt5.QtWidgets  import QApplication , QWidget  , QLabel , QLineEdit
import sys
from PyQt5.QtGui import  QPixmap

app =QApplication(sys.argv)
window = QWidget()

lable = QLabel(window)
pixmap = QPixmap(r'C:\Users\kira\Desktop\834364.jpg')
window.resize(pixmap.width() , pixmap.height())
lable.setPixmap(pixmap)
line = QLineEdit(window)
window.show()
sys.exit(app.exec_())