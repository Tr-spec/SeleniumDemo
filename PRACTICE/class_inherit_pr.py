from PRACTICE.def_inheritance import Baseclass, My_class


class BaseClass2(My_class):


    def new_1(self, a, b):
        return a * b


mc = BaseClass2()
new = mc.new_1(10, 500)
print(new)

mc.my_func_2()
mc.set_1()

















