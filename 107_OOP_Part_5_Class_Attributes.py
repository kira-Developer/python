# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------

class member :
    not_allowed = ['hell' , 'shit' ,'baloot']
    users_num = 0

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

