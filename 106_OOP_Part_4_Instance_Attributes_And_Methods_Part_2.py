# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------
class member :
 def __init__(self , first_name , middle_name , last_name , gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

 def full_name (self) :
    return f'{self.fname} {self.mname} {self.lname}'

 def name_with_title(self) :
         if self.gender == 'male' :return f'hello mr {self.fname}'
         elif self.gender == 'female' :return f'hello miss {self.fanme}'
         else :return f'hello {self.fname}'

 def get_all_info(self) :
    return f'{self.name_with_title()}, your full name is : {self.full_name()}'

member_one = member('abdullh' , 'bander' , 'alosami' , 'male')


print(member_one.get_all_info())


