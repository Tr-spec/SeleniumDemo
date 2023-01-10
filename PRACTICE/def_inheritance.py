
class Baseclass:

    def my_func_1(self):
        print("This is func 1 from Baseclass")


    def my_func_2(self):
        print("This is func 2 Baseclass")


class My_class(Baseclass):

    def set_1(self):
        print("This is inherited from Baseclass and this is My_class")

    def set_2(self):
        print("This is inherited 2 from Baseclass and this is My_class")


bs = Baseclass()
bs.my_func_2()

mc = My_class()
mc.my_func_1()
mc.set_1()

