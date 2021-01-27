# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# Test Word [ WWWoooorrrldd ] # print(x[1:])


def cleanword(word):
    if len(word) == 1 :
        return  word
    if word[0] == word[1] :
        return  cleanword(word[1:])
    return word[0] + cleanword(word[1:])
  # Stash [ kira ]
print(cleanword('kkkirrrrraaa'))