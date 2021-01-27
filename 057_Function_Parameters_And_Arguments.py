# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------


a , b  = 'kira' , 'abdullh'


print(f'hello {a}')
print(f'hello {b}')

print('=' * 50)

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("kira")      => kira is The Argument

def say_hello(n):

    print(n)

say_hello('kira')
say_hello(b)

print('=' * 50)

def addition(n1 , n2) :
    print(n1 + n2)

addition(100 ,300)
addition(-50 , 100)
print('=' * 50)
def addition(n1 , n2 ) :
    if type(n1) != int or type(n2) != int :
        
        print('only integers')

    else :
         print(n1 + n2) 

addition(100 , 300)

def full_name(first , middle , last ) :
    
    print(f'hello {first.strip().capitalize()} {middle.strip().capitalize()} {last.strip().capitalize()}')


full_name('kira' , 'abdullh' , 'kira')
