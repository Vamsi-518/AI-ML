"""
###file operations
#file Handling  csv file

#create a class employee having empno,ename and sal as instance variables
#define doing/knowing responsibilities for the entity
#create a class company having entity list and set  of operations on it
#on landing the software all existing employee data should be loaded from "emdata.scv" file to the company

import csv
class Employee:
    noofemployees = 0
    def __init__(self, empno, ename, sal):
        self.empno = empno
        self.ename = ename
        self.sal = float(sal)
        Employee.noofemployees += 1
    def getempno(self):
        return self.empno
    def getename(self):
        return self.ename
    def getsal(self):
        return self.sal
    def setename(self, ename):
        self.ename = ename
    def setsal(self, sal):
        self.sal = sal

    @staticmethod
    def getnoofemployees():
        return Employee.noofemployees
class Company:
    def __init__(self):
        self.companyname = "soft tech"
        self.emplist = []
    def loademployees(self, filename):
        with open(filename, "r") as f:
            csvReader = csv.reader(f)
            header = next(csvReader)
            for row in csvReader:
                empno = row[0]
                ename = row[1]
                sal = row[2]
                e = Employee(empno, ename, sal)
                self.emplist.append(e)
    def displayemployees(self):
        for e in self.emplist:
            print(
                e.getempno(),
                ",",
                e.getename(),
                ",",
                e.getsal()
            )
if __name__ == '__main__':
    c = Company()
    c.loademployees("empData.csv")
    c.displayemployees()
    print("Total Employees:",
          Employee.getnoofemployees())
"""