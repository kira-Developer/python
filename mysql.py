
# import library
import pymysql

class connect:
  def __init__(self):
   try:
     # database arg

      host = "localhost"
      user = 'root'
      password = ''
      dbName = 'python'

      # connction

      db = pymysql.connect(host=host, user=user, password=password, db=dbName)

      # print if connection success

      print("connection Success")


   except pymysql.err as errors :

              print(f"filed connecting {errors}")



connects = connect()


