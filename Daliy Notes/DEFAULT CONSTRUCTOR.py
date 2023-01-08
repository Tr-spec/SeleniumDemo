#
#
# class Sales:
#     Id = 101
#     Name = "Swapnil"
#     Company = "Capgemini"
#     Salary = "9000000"
#
#     def __int__(self,id,name,company,salary):
#         self.Id = id
#         self.Name = name
#         self.Company = company
#         self.Salary = salary
#
#
#     def getSales(self):
#         return (f"Id = {self.Id}, Name = {self.Name}, Company = {self.Company}, Salary = {self.Salary}")
#
#     @staticmethod
#     def programstatus():
#         return "Program Completed"
#
#
# temp = Sales()
#
#
#
#
# class Employee:
#
#     name = "swapnil"        # CLASS LEVEL ATTRIBUTE
#     id = 101
#     city = "Nagpur"
#                                                             # OBJECT LEVEL ATTRIBUTE
#     def __init__(self,name = "swapnil",id = 101,city = "USA",Grade = "Unknown"):
#         self.name = name
#         self.id = id
#         self.city = city
#         self.Grade = Grade      # OBJECT LEVEL ATTRIBUTE
#
#     def getempdeatils(self):
#         return (f"name= {self.name}, id = {self.id}, city = {self.city}, Grade = {self.Grade}")
#
#     @staticmethod
#     def empAdd():
#         return "Unidentified"
#
# temp = Employee()
# print(temp.getempdeatils())
# print(temp.empAdd())
#
# temp2 = Employee("Sagar",1500,"Pune","A+")
# print(temp2.getempdeatils())
# print(temp2.empAdd())
#
# temp3 = Employee("tushar",108,"Mumbai")
# print(temp3.getempdeatils())
# print(temp3.empAdd())
#
#
#
#
# avalue = "wel3434co332m234555e"
#
# emp_str = ""
# for i in avalue:
#     if i.isdigit():
#         emp_str = emp_str + i
# print(emp_str)
#
# sum =1
# for i in avalue:
#     if i.isdigit():
#         sum = sum + int(i)
# print(sum)
#
# emp_str = ""
# for i in avalue:
#     if i.isalpha():
#         emp_str = emp_str + i
# print(emp_str)
#
#
# # Print Even Numbers
# n = int(input("Enter Value : "))
# for i in range(0, n+1):
#     if i % 2 == 0:
#         print("Even Numbers = ", i)
#
# # Print Odd Numbers
# for i in range(0, 101):
#     if i % 2 != 0:
#         print("Odd Numbers = ", i)
#
#
# ilist = [10,20,20,78,54,55,44,33,11,17,19,20]
#
# for i in ilist:
#     if i % 2 == 0:
#         continue
#     print("Odd Numbers from ilist = ", i)
#
#
# #Print Upto 78
# for i in ilist:
#     if i == 78:
#         break
#     print(i)
#
#
# #Table 0f 10
#
#
# icounter = 1
# while icounter <= 10:
#     print(f"10 * {icounter} = {10 * icounter}")
#     icounter = icounter + 1
#
#

## DEFAULT PARAMETER
# class Vechilereg:
#
#     def __init__(self, vehicleid=100, vehicletype="not known", vehiclename="unknown"):
#         self.vehicleid = vehicleid
#         self.vehicletype = vehicletype
#         self.vehiclename = vehiclename
#
#     def getVehicleDetails(self):
#         return (f"vehicleid = {self.vehicleid}, vehicletype = {self.vehicletype}, , vehiclename ={self.vehiclename}")
#
#
# reg = Vechilereg()
# print(reg.getVehicleDetails())
#
# reg2 = Vechilereg(150, "two wheeler", "activa")
# print(reg2.getVehicleDetails())
#
# print(reg.getVehicleDetails())
#
# reg.vehiclename = "shine"
# print(reg.getVehicleDetails())
#
# print(reg.getVehicleDetails())
#
# reg = Vechilereg()  ## RESET MODE
# print(reg.getVehicleDetails())


# Mainstring = input("Enter String : ")
# Substring = input("Enter Substring : ")
#
# first_index = Mainstring.index(Substring)
# second_index = Mainstring.index(Substring, first_index + 1)
# third_index = Mainstring.index(Substring, second_index + 1)
#
# print(f"Substring {Substring} from {Mainstring} is {third_index}")


# class Calculator:
#
#     def __init__(self, first_num = 200, second_num = 300):
#         self.first_num = first_num
#         self.second_num = second_num
#
#     def getAddition(self):
#         return self.first_num + self.second_num
#
#     def getSubtraction(self):
#         return self.first_num - self.second_num
#
#     def getMultiplication(self):
#         return self.first_num * self.second_num
#
#     def getDivision(self):
#         return self.first_num / self.second_num
#
#     @staticmethod
#     def getUpdate():
#         print("Program Completed")
#
# result = Calculator()
# print(result.getAddition())
#
# print(result.getUpdate())
#
# result = Calculator(500, 500)
# print(result.getMultiplication())
# print(result.getUpdate())


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
#
# driver.get("https://www.facebook.com")
#
# driver.maximize_window()
#
#
# emailElement = driver.find_element(By.XPATH, "//input[@id='email']")
# emailElement.send_keys("www.shastrakar123@reddiff.com")
#
# passElement = driver.find_element(By.XPATH, "//input[@id='pass']")
# passElement.send_keys("121121")
#
# logElement = driver.find_element(By.NAME, "login")
# logElement.click()
#
# time.sleep(2)
# driver.back()

c = 200  # global variables
d = 200


class MyClass:
    x, y = 500, 500  # class variables or attributes

    def add(self, a=1, b=1):
        print(a + b)  # local variables
        print(self.x + self.y)
        print(c + d)


mc = MyClass()
print(mc.add())

##=================================================

class Myclass:

    def __init__(self, firstnum=300, secondnum=200):
        self.firstnum = firstnum
        self.secondnum = secondnum

    def add(self):
        return self.firstnum + self.secondnum

    def sub(self):
        return self.firstnum - self.secondnum


mc = Myclass()
print(mc.add())
print(mc.sub())
