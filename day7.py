"""
from tkinter import *

class Table:
    def __init__(self, root):
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):            
                if (i == 0):
                    self.data = Entry(root, width=20, fg='red', font=('Arial', 18, 'bold'))
                    self.data.grid(row=i, column=j)
                    self.data.insert(END, lst[i][j])
                else:
                    self.data = Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold'))
                    self.data.grid(row=i, column=j)
                    self.data.insert(END, lst[i][j])
lst = [
    ("Empno", "Ename", "Salary"),
    (101, "AAA", 10000),
    (102, "BBB", 50000),
    (103, "CCC", 75000),
    (104, "DDD", 85000),
    (105, "EEE", 90000)
]
total_rows = len(lst)
total_columns = len(lst[0])
root = Tk()
t = Table(root)
root.mainloop()
"""


                