# firstNum = 150
# secondNum = 100
#
#
# class my_class:
#     global firstNum
#     global secondNum
#
#     def add_func(self):
#         firstNum = 200
#         secondNum = 334
#         print(firstNum + secondNum)
#
#
# mc = my_class()
# mc.add_func()


# class my_selenium:
#
#     def __init__(self, firstnum, secondnum):
#         self.firstNum = firstnum
#         self.secondNum = secondnum
#
#     def add_cls(self):
#         print(self.firstNum + self.secondNum)
#
#
# mc = my_selenium(454, 334.3)
# mc.add_cls()
#
# mc2 = my_selenium(86, 78)
# mc2.add_cls()
#
# mc3 = my_selenium(30.9, 99.98)
# mc3.add_cls()


class my_class:
    name = "swapnil"
    salary = 1000000
    profession = "Automation QA"

    def info_1(self):
        print(f"name = {self.name}, salary = {self.salary}, profession = {self.profession}")


mc1 = my_class()
mc1.info_1()

mc1.salary = 12000000
mc1.info_1()
mc2 = my_class()
mc2.info_1()

print(mc1.salary)


str = "wel22co3r23me"

sum = 0
for i in str:
    if i.isdigit():
        sum = sum + int(i)
print(sum)






