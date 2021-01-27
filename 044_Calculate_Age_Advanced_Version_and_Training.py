# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# write note

print("#" * 80)
print(' you can write the first lertter or full name of the time unit '.center(80  , '#'))
print("#" * 80)

# input Age

age = int(input('what\'s age ?').strip())
# collect time unit data


uint = input("please choose time unit : months weeks days").strip().lower()

# Get time uints

months = int(age) * 12
weeks = months * 4
days = int(age) * 365

print('You lived for :')

if uint == 'months' or uint == "m" :
    print(f'your age in months is {months}')


elif uint == 'weeks' or  uint == "w" :
      print(f'your age in weeks is {weeks}')



elif uint == 'days' or  uint == "d" :
  print(f'your age in days is {days}')
