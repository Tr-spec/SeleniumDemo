
# In oops everything is considered as object
class Emp:
    def __init__(self, eid, ename, sal):
        self.eid1 = eid
        self.eid = self.eid1
        self.ename = ename
        self.sal = sal
        print("This is a parameterized constructor")

    def display(self):
        print(f"Eid : {self.eid}, Ename : {self.ename}, Esal : {self.sal}")

    @staticmethod
    def update():
        print("This is a static method")

mc = Emp(100, "swapnil", 900000)
mc.display()

mc2 = Emp(200,"tushar",100000)
mc2.display()

mc.update()
