# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) =>
# ------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()
# cerate the tables and fields

cr.execute('create table if not exists users(user_id integer , name text)')
cr.execute('create table if not exists countries(id integer , countries_name text)')
# inserting Data

# cr.execute('insert into users(user_id , name) values(\'1\' , \'abdlluh\')')
# cr.execute('insert into users(user_id , name) values(\'2\' , \'kira\')')
# cr.execute('insert into users(user_id , name) values(\'3\' , \'ner\')')

# fetch data

users = cr.execute('select user_id,name from users')

print(cr.fetchone())

print(cr.fetchmany(2))

print(cr.fetchall() )

# Save (Commit) Changes
db.commit()

# Close Database
db.close()