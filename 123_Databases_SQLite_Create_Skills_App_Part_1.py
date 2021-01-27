# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 1 --
# -----------------------------------------------------

# import sqlit3 module

import sqlite3

# create database and connect
db = sqlite3.connect('app.db')

#setting  up the cursor
cr = db.cursor()
# commit and close method

def commit_and_close():

  # save (commit) changes
  db.commit()

  # close database
  db.close()
  print("connection to database is closed")

# my user ID
uid = 1


# input pig message
input_message = """
what do you want to do
"s" => show all skills 
"a" => add new skill
"d" => delete a skill
"u" update skill progress
"q" => quit the app
shoose option:
"""
# input option choose
user_input = input(input_message).strip().lower()

# command list

commands_list = ['s' , 'a' , 'd' , 'u' , 'q']

# define the methods
def show_skills():
  cr.execute(f"select * from skills where user_id = {uid}")
  results = cr.fetchall()

  if len(results) > 0 :
    print(f"you have {len(results)} skills")
    print("showing skills with progress: ")

    for row in results:
      print(f"skill => {row[0]},", end=" ")
      print(f"progress => {row[1]}%")

  else: print("you not have any skill")


  commit_and_close()

def add_skill():
  sk = input("write skill Name :").strip().capitalize()
  prog = input("write skill progress :").strip()
  cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
  commit_and_close()

def delete_skill():
  sk = input("write skill Name :").strip().capitalize()

  cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
  commit_and_close()

def update_skill():
  sk = input("write skill Name :").strip().capitalize()
  new_prog = input("write skill  new progress :").strip()
  cr.execute(f"update skills  set progress = '{new_prog}'  where name = '{sk}' and user_id = '{uid}'")
  commit_and_close()

# check if command is exists

if user_input in commands_list :


  if user_input == 's':
    show_skills()
  if user_input == 'a':
    add_skill()
  if user_input == 'd':
    delete_skill()
  if user_input == 'u':
    update_skill()
  else: exit()

else:
  print(f"sorry this command \"{user_input}\" is not Found")

