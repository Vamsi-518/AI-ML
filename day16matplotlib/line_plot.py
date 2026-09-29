#Matplotlib is a Python library used to create graphs and visualizations.
import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
marks = [60, 70, 75, 85, 90]
plt.plot(days, marks)
plt.title("Student Marks")
plt.xlabel("Days")
plt.ylabel("Marks")
plt.show()