print(1,2,3,4)

mylist = [1 , 2,3 ,4, 5]

print(mylist)
print(*mylist)

print('=' * 50)

def say_hello(*peoples):

  for name in peoples :
    print(f'hello {name}')


say_hello('abdullh' , 'kira' , 'none')


print('=' * 50)

def show_details(skill1 , skill2 , skill3 ) :
    
        print(f'{skill1}') 
        print(f'{skill2}')
        print(f'{skill3}')

show_details('html' , 'php' , 'js')

print('=' * 50)

def show_details(*skills):
    
    for skill in skills :
        print(skill)

show_details('python' , 'js' , 'html' , 'php')
