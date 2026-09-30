import matplotlib.pyplot as plt
students = ["Krishna", "Rahul", "Arjun", "Vijay"]
marks = [85, 72, 91, 65]
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("student_marks.png")
plt.show()