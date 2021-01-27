# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------


class Member :
    def __init__(self , name , age):
        # var
        self.name = name
        self.age = age

    def say_hello(self) :
        return f"hello {self.name}"
    @property
    def age_in_days(self):
        return self.age * 365


one = Member("abdullh" , 17)

print(one.name)
print(one.age)
print(one.say_hello())

print(one.age_in_days)
