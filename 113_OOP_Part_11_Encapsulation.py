# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------



class Member :
    def __init__(self , name):
        self._name  =  name # public


one = Member("abdullh")

print(one._name)

one._name = "bander"

print(one._name)


class Member2 :

    def __init__(self, name):
        self.__name = name  # Private

    def say_hello(self):
        return f"Hello {self.__name}"
two = Member2('abdullh')

print(two.say_hello())

