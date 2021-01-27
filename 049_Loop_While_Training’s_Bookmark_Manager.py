# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------


# empty list to fill later

myfavouritewebs = []

# maximum allowed websires
maximumwebs = 5

while maximumwebs > 0:

    # input the new website
    web = input('website name without https://')

    # add the new website to the list

    myfavouritewebs.append(f"https://{web.strip().lower()}")

    # decrease one number from allowed websites
    maximumwebs -= 1  # maximumwebs = maximumwebs - 1
    # print the add message
    print(f"website added , {maximumwebs} places left")

    # print the list
    print(myfavouritewebs)
else:
    print('bookmark is full, you can\' add more')
