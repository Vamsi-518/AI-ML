import matplotlib.pyplot as plt
students = ["Krishna", "Rahul", "Arjun", "Vijay"]
marks = [85, 72, 91, 65]
plt.barh(students, marks)
plt.title("Student Marks")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()