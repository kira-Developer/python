# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------
from abc import ABCMeta , abstractclassmethod
class Programming(metaclass=ABCMeta) :
    @abstractclassmethod
    def has_oop(self):
        pass

class Python(Programming) :
    def has_oop(self):
        return  "Yes"


class Pascla(Programming) :

    def has_oop(self):

        return "No"


one = Python()
print(one.has_oop())