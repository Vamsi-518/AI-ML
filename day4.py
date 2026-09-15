"""
##day4
#oop using python

class employee:
    def __init__ (self,empid,empname,sal):
        self.empno= empid
        self.ename=empname
        self.sal=sal
        employee.noOfemployees = employee.noOfemployees + 1

def getempno(self):
    return self.empno
def getename(self):
    return self.ename
def getsal(self):
    return self.sal
def setename(self,ename):
    self.ename=ename
def setsal(self,sal):
    self.sal=sal
@staticmethod
def getemployees():
    return employee.noofemployees
if(__name__=='__main__'):
    e=employee(201,"vamsi",100000)
    e1=employee(202,"naga",50000)
    print("first employee:",e.getempno(),",",e.getename(),",",e.getsal())
    print("second employee:",e1.getempno(),",",e1.getename(),",",e1.getsal())
    print("total number of employees:",employee.getemployees)

"""
"""
#inheritance depicts is a relationship where the sub-entity specializes

class A:
    def __init__ (self,a):
        print("In A constructor")
        self.a= a
    def show(self):
        return self.a
class B(A):
    def __init__ (self,a,b):
        self.b=b
        print("In the B class initializer")
        super(). __init__(a)
    def show(self):
        return self.a + self.b
if(__name__== '__main__'):
    b=B(250,300)
    print("the sum is:",b.show())
"""
