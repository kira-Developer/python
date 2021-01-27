import mysql.connector

db = mysql.connector.connect(user='root' , password='' , host='localhost' , database='python')
cr =db.cursor()

cr.execute('show tables')
print(cr.fetchall())