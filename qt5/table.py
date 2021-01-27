import sys , sqlite3
from PyQt5.QtWidgets import QApplication , QTableWidget , QTableWidgetItem , QWidget , QMenuBar ,QAction

# connect databaes

db = sqlite3.connect('../app.db')
cr = db.cursor()
cr.execute('select * from skills')
result= cr.fetchall()
db.commit()

# set app
app = QApplication(sys.argv)
window = QWidget()

# function
def add_item():
  from PyQt5.QtWidgets import QLineEdit , QLabel , QPushButton
  # set socund window

  newWindow = QWidget()

  # set label

  lable1 = QLabel('name' ,newWindow)
  lable2 = QLabel('progress', newWindow)

  # lable pro
  lable1.setGeometry(180 , 40 , 47 , 21)
  lable2.setGeometry(180, 100, 47, 21)

  # set input
  line1 = QLineEdit(newWindow)
  line2 = QLineEdit(newWindow)
  # input pro

  line1.setGeometry(70, 70, 261, 20)
  line2.setGeometry(70 , 120 , 261 ,20)

  button = QPushButton('insert' , newWindow)
  button.setGeometry(150 , 170 ,101 , 23)

  def insert():
    cr.execute(f"insert into skills(name, progress, user_id) values('{line1.text()}', '{line2.text()}', '1')")
    db.commit()

  button.clicked.connect(insert)

  newWindow.setGeometry(50 , 50 ,400 , 300)

  newWindow.show()
  sys.exit(app.exec_())
# menu
menu = QMenuBar(window)
dbMenu = menu.addMenu('db')
item = QAction('insert' , window)
item2 = QAction('ref' , window)
item.setShortcut("ctrl+a")
item2.setShortcut("ctrl+s")
item.triggered.connect(add_item)
dbMenu.addAction(item)
dbMenu.addAction(item2)

# set title
window.setWindowTitle("table")
window.setGeometry(0 , 0 ,500 , 500)
# table
table = QTableWidget(window)

table.setColumnCount(3)
table.setGeometry(20 , 20 , 500 , 500)

for row_number , user in enumerate(result):
  table.insertRow(row_number)
  for column_number , data in enumerate(user):
    cell = QTableWidgetItem(str(data))
    table.setItem(row_number , column_number ,cell)

table.setHorizontalHeaderLabels(str('name Progress user_id').split(' '))


window.show()



sys.exit(app.exec_())