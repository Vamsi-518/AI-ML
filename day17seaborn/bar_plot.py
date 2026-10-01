import seaborn as sns
import matplotlib.pyplot as plt
students = ["Krishna", "Rahul", "Arjun", "Vijay"]
marks = [85, 72, 91, 65]
sns.barplot(x=students, y=marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()