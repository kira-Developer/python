# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------


# sum(iterable, start)
a = [1 , 2 , 3 ,4 , 30]
print(sum(a , 40))

# round(number, numofdigits)
print(round(150.499))
print(round(150.34 , 2))

# range(start, end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0 , 20 , 2)))


# print()

print('hello abdullh')
print('hello' , 'abdullh')
print('hello' , 'abdullh' , 'how' , 'are' , 'you' , sep='|')

print('first line' , end='\n')
print('second line')