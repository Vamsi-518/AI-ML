#                                  ****DAY_TWO****
"""
#list comprehension 
list=[10,20,30,40,50,60,70]

#to create another list

list2=[]
for x in list:
    if(x>30):
        list2.append(x)
print("the new list is: ",list2)

#using list compreshension
list3=[x for x in list if(x>30)]
print(list3)

list=[20,True,35,False]
print(list[1])
print(list[2])

"""
"""
#function in list
#set:set is an unordered collection of elements.
aset ={100,200,30,40,50,90,100,200}
print(aset)
bset={300,100,200,75,65,55,35}
print(aset.union(bset))
print(aset.intersection(bset))
print(aset - bset)
#Dictionary:represented with a key value pair wher where is key is unique
a={"one":1,"two":2}
print(a["two"])
print(a.get("two"))
print(a.keys())
print(a.values())
for i in a:
    print(i)
for i in a:
    print(a[i])
#Tuples:an immutable row/record ()
rec=()
print(type(rec))

empDB=[(201,"aaa",50000),(202,"bbb",100000),(203,"ccc",200000)]
print(empDB[1])
print(empDB[1][2])
"""
"""

#Functions:to compartmentalize asepecfic task or action or anaspet of business
def functionName(arg1,arg2):
    #body of the func
    #return stat
#To call a func:
#implement an employee insert and display operation
#employee :list
#records of emp as tuple(empno,ename,sal) 
"""
"""
def insertRecords(empdb , rec):
    empdb.append(rec)
def displayAllEmployee(empdb):
    cnt =1
    for rec in empdb:
        print("Employee",cnt,"#",rec[0],"",rec[1],"",rec[2])
        cnt =cnt + 1
def getEmpDetails(empdb):
    print("provide Employee Details:")
    empno=int(input("Empno:"))
    ename=input("Ename:")
    sal = int(input("salary:"))
    rec=(empno,ename,sal)
    no = insertRecords(empdb,rec)
    print(no,"record insetted")
def viewmenu(empdb):
    cont="y"
    while(cont == "y"):
        print("1:insert a record\n2: Display all record\n0: to exit")
        res= int(input("your choice:"))
        if(res == 1):
            getEmpDetails(empdb)
        elif(res == 2):
            displayAllEmployee(empdb)
        elif(res==0):
            cont="n"
        else:
            print("Invalid choice")
empdb=[]
viewmenu(empdb)
"""
"""
###Anonymous functions using lambda
def cubeTest(y):
    return y*y*y
cubeTest(5)

ret = lambda y:y*y*y
ret(5)

"""
"""
strlist =["this","is","a","session","of","ai/ml"]
len(strlist)

strlist2=list(map(lambda s:s.upper()+"!",strlist))
print(strlist2)

retval = lambda x:x*2 if x<5 else x
retval(4)
strlist3=list(filter(lambda s:len(s)>3,strlist))
print(strlist3)
"""

