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
    def __init__(self , first_name , middle_name , last_name):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name




member_one = member('abdullh' , 'bander' , 'alosami')


print(member_one.fname , member_one.mname , member_one.lname , sep='\n')
