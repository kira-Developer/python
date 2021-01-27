# import Library
import sys , sqlite3
from PyQt5.QtWidgets import QApplication ,QWidget , QPushButton , QLabel

# database conneceting
db = sqlite3.connect('../app.db')

def dataShow() :
  cr = db.cursor()
  cr.execute("select * from skills")
  result = cr.fetchall()
  for skill in result :
   lable.setText(skill[0])
   print(skill[0])
  db.commit()
  db.close()

#  window
app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(100 , 100 , 500 , 500)

# set button
button = QPushButton('show all data' , window)
button.move(200 , 300)
# set lable
lable = QLabel('result' , window)
lable.setGeometry(200 , 200 , 600 , 100)
# evint
button.clicked.connect(dataShow)
# show window
window.show()
sys.exit(app.exec_())
