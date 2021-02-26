import random

class Employees:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def employee_info(self):
        return f"This employee is {self.fname} {self.lname}."

    # property created
    @property
    def email_creater(self):
        if self.fname is None or self.lname is None:
            return "The employee is invalid . Check the data!"

        return f"The email of employee is : {self.fname}.{self.lname}{random.randint(1, 9)}@gmail.com"

    # property setter for chnaging the values
    @email_creater.setter
    def email_creater(self, string):
        print("Setting now ....")
        names = string.split("@")[0]
        self.fname = names.split(".")[1]
        self.lname = names.split(".")[0]

    # property deleter for deleting the values
    @email_creater.deleter
    def email(self):
        self.fname = None
        self.lname = None
        return f"The is email is deleted"


fname = str(input("Enter your first name : "))
lname = str(input("Enter your last name : "))
Rihan = Employees(fname, lname)
print(Rihan.employee_info())
print(Rihan.email_creater)
Rihan.email_creater = "wasi.bagwan@codeharry.com"
print(Rihan.email_creater)

