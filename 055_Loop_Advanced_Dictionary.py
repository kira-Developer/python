# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------
myskills = {
        "html" : "80%" ,
        "css"  : "40%",
        "js"   : "60%",
        "php"  : "60%",
        }

print(myskills.items())

myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key, main_value in myUltimateSkills.items():

  print(f"{main_key} Progress Is: ")

  for child_key, child_value in main_value.items():

    print(f"- {child_key} => {child_value}")
