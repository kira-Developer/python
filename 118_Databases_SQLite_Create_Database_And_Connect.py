# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------
# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")
# Create The Tables and Fields
db.execute("CREATE TABLE if not exists skills (name text , progress integer , user_id integer)")



db.close()