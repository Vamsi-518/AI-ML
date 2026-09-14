#lambda func using reduce
"""
list=[50,24,556,25,200,115,]
#To find out the highest number using lambda func and reduce
from functools import reduce
highestNumber = reduce(lambda a,b : a if a>b else b,list)
print("The greatese value is:",highestNumber)
sortedlist=sorted(list)
print(sortedlist)
sortedlist = sorted(list,reverse =True)
print(sortedlist)

listdata=[("aaa",201),("nnn",20),("lll",99),("kkk",808)]
listtest=sorted(listdata)
print(listtest)

sorteddata=sorted(listdata,key=lambda x:x[1])
print(sorteddata)

empids=['cs101','tt050','ecs030','it001']
sortedids=sorted(empids,key=lambda x:int(x[2:]))
print(sortedids)
"""
"""
#working with datetime object

import datetime
dt=datetime.datetime.now()
print(dt)

dt2=datetime.date.today()
print(dt2)
print("current year:",dt2.year)
print("current month:",dt2.month)
print("current day:",dt2.day)

#two useful func:strftime() and strptime() for formatimg
import datetime
from datetime import datetime
dt1 = datetime.now()
strdate= dt1.strftime("%d/%m/%y, %H:%M:%S")
print(strdate)
"""

    


