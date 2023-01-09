
class Baseclass:

    def my_func_1(self):
        print("This is func 1")


    def my_func_2(self):
        print("This is func 2")


class My_class(Baseclass):

    def set_1(self):
        print("This is inherited")

    def set_2(self):
        print("This is inherited 2")


bs = Baseclass()
bs.my_func_2()

mc = My_class()
mc.my_func_1()
mc.set_1()

