from PyQt5.QtWidgets  import QApplication , QWidget ,QComboBox ,QCalendarWidget
import sys


app =QApplication(sys.argv)
window = QWidget()
co = QComboBox(window)
lists = [1, 2 , 3 , 4 , 5]
for list in lists :
  co.addItem(str(list))
window.setGeometry(100 , 200 , 400 ,400)
coo = QCalendarWidget(window)
window.show()
sys.exit(app.exec_())