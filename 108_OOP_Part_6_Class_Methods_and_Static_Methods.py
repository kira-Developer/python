# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------


class member :
    not_allowed = ['hell' , 'shit' ,'baloot']
    users_num = 0
    @classmethod
    def show_user_count(cls):
        print(f'we have {cls.users_num} users in our system')
    @staticmethod
    def say_hello():
        print('hello from static method')
    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        member.users_num += 1 # member.users_num = member.users_num + 1
    def full_name(self):

        if self.fname in member.not_allowed :
            raise ValueError('name not allowed')
        else :
         return f'{self.fname} {self.mname} {self.lname}'

    def name_with_title(self):
        if self.gender == 'male':
            return f'hello mr {self.fname}'
        elif self.gender == 'female':
            return f'hello miss {self.fanme}'
        else:
            return f'hello {self.fname}'

    def get_all_info(self):
        return f'{self.name_with_title()}, your full name is : {self.full_name()}'
    def delete_user(self):
        member.users_num -= 1
        return f'user {self.fname} deleted'

member_one = member('abdullh', 'bander', 'alosami', 'male')
print(member.users_num)
print(member_one.delete_user())
print(member.users_num)
print('#' * 50)
member.show_user_count()
member.say_hello()