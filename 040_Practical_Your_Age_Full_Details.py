# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------


# input age

age = int(input('what\'s your age?').strip())

# get age in all time uints
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60 
seconds = minutes * 60 
print(f'you lived for: \n{months} months  \n{weeks:,} weeks  \n{days:,} days  \n{hours:,} hours  \n{minutes:,} minutes  \n{seconds:,} seconds')