# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------


import sqlite3

def get_all_data() :
  try:
    # Connect To Database
    db = sqlite3.connect("app.db")

    # Print Success Message
    print("Connected To Database Successfully")

    # Setting Up The Cursor
    cr = db.cursor()

    # Fetch Data From Database
    cr.execute("select * from users")

    # assign data to variable
    results = cr.fetchall()
    # print number of rows
    print(f"database has {len(results)} rows.")

    # printing message
    print("showing Data: ")

    # loop on results
    for row in results :
      print(f"userID =>{row[0]}," , end= " ")
      print(f"username => {row[1]}")

  except sqlite3.Error as error :
    print(f'error reading data{error}')

  finally:
    if (db) :

      # close database connection
      db.close()

      print("connection to database is closed")

get_all_data()