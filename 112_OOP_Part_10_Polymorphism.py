# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------
n1 = 10
n2 = 20
print(n1 + n2)
s1 = "Hello"
s2 = "Python"

print(s1 + s2)

print(len([1, 2, 3, 4, 5]))
print(len('abdullh'))
print(len({'key_one': 1, 'key_two': 2}))


class A:
    def do_something(self):
        print("from class A")

        raise NotADirectoryError("Derived Class Must Implement This Method")


class B(A):
    def do_something(self):
        print("from class B")


class C(B):
    def do_something(self):
        print("from class C")


my_instance = B()
my_instance.do_something()
