# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# seting up the cursor
cr = db.cursor()

# update data
cr.execute("update users set name = 'test' where user_id = 1")

# delete data
cr.execute("delete from users where user_id = 3")
# fetch data
cr.execute("select * from users")

print(cr.fetchall())
# save (commit) changes
db.commit()

# close database
db.close()
