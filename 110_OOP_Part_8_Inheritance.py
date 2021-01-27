# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food :
    def __init__(self, name , price):
        self.name = name
        self.price = price



        print(f"{self.name} Is Created From Base Class")

    def eat(self) :
         print("Eat Method From Base Class")



class Apple(Food) :
        def __init__(self ,name , price , amount):
       # Food.__init__(self,name) # create instance from base class
         self.amount = amount
         super().__init__(name , price)


         print(f"{self.name} Is Created From Derived Class and price is {self.price} And Amount Is {self.amount}")
            



Food_one = Apple("Pizza" , 140)
# Food_two  = Apple()
# Food_two.eat()




