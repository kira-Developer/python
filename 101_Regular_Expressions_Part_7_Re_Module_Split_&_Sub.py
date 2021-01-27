# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------

import re

string_one  = 'love python'

search_one = re.split(r'\s' , string_one ,1)

print(search_one)

print('#' * 50)

string_two = 'how-to_write_a_very-good-article'
search_two = re.split(r'-|_' , string_two)
print(search_two)

print('#' * 50)
# get words from URL
for word in search_two :
    if len(word) ==1 :
        continue
    print(word)
print('#' * 50)
print(re.sub(r'\s' , '-'  , string_one))