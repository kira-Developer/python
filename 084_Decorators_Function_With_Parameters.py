# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def decorator(func) :
    def nestedfunc(num1  , num2) :  # any name its just for decoration
       if num1 < 0 or num2 < 0 :
            print('beware on of the numbers os less than zero')

       func(num1 , num2)  # execute function
    return nestedfunc  # return all data

@decorator
def calculate(n1  , n2) :
        print(n1 + n2)

calculate(-5 , 300)