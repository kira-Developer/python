import mysql.connector
class database():
  def connect(self):
    db = mysql.connector.connect(user='root', password='', host='localhost', database='python')
    return db
  def get_user(self):
    con = self.connect()
    cr = con.cursor()
    query = "select * from user_information"
    try:
      cr.execute(query)
      list_data = cr.fetchall()
    except Exception as err:
      print(err)
      return None
    finally:
      cr.close()
  def check_user(self , user , passWord):
    data = self.get_user()
    uesrname = []
    password = []
    for i in data:
      uesrname.append(i[2])
      uesrname.append(i[5])
      Len = 0
      while Len < len(uesrname):
        if uesrname[Len] == user :
          if password == passWord :
            return 0
          else: return 1
        else:
          Len += 1
          continue
          return 3

