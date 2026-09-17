"""
#Exception Handling in python
#keywords related to exception:
#try,except,else,finally,raise
try:
    num=int(input("Enter numerator"))
    den=int(input("Enter denumerator"))
    val=num/den
    print("The value is:",val)
except ZeroDivisionError,ValueError:
    print("corrective Action: using default value")
    den=10
    val=num/den
    print("The value is:",val)
else:
    print("The value is:",val)
finally:
    print("Executing finally")

"""
"""
class salaryExcept(Exception):
    def __init__(self,sal):
        print("Two Low Salary",sal)
class emp:
    def __init__(self,empno,ename,sal):
        try:
           self.__empno=empno
           self.__ename=ename
           self.__sal=sal
           if(self.__sal<30000):
               raise salaryExcept(sal)
        except salaryExcept:
            print("salary exception occurred. using default value")
            self.__sal=30000
    def getempno(self):
        return self.__empno
    def getename(self):
        return self.__ename
    def getsal(self):
        return self.__sal
if(__name__ =='__main__'):
    e1=emp(201,"vamsi",5000)
    e2=emp(202,"naga",45000)
    print("employee1 details:",e1.getempno(),":",e1.getename(),":",e1.getsal())
    print("employee2 details:",e2.getempno(),":",e2.getename(),":",e2.getsal())
"""