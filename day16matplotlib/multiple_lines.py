import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
python_marks = [60, 70, 75, 85, 90]
sql_marks = [55, 65, 70, 80, 85]
plt.plot(days, python_marks, label="Python")
plt.plot(days, sql_marks, label="SQL")
plt.title("Python vs SQL")
plt.xlabel("Days")
plt.ylabel("Marks")
plt.legend()
plt.show()