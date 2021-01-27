from  PyQt5.QtWidgets  import QApplication  , QWidget , QTabWidget , QPushButton
import sys

app = QApplication(sys.argv)
window = QWidget()

tab = QTabWidget(window)
tab.resize(400 , 400)
one = QWidget()
two = QWidget()
three = QWidget()
list = [one , two ,three]


for key,tabs   in enumerate(range(7)):

  tabs =QWidget()
  tab.addTab(tabs ,str(key +1))
  button = QPushButton(f'hello insert {key +1}' , tabs)
  button.move(10 ,40)
window.setGeometry(299 , 399 , 400 , 499)
window.show()
sys.exit(app.exec_())