import seaborn as sns
import matplotlib.pyplot as plt
courses = [
    "Python",
    "Java",
    "Python",
    "SQL",
    "Python",
    "Java"
]
sns.countplot(x=courses)
plt.title("Course Count")
plt.xlabel("Course")
plt.ylabel("Number of Students")
plt.show()