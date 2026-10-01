import seaborn as sns
import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
marks = [60, 70, 75, 85, 90]
sns.lineplot(x=days, y=marks)
plt.title("Student Marks")
plt.xlabel("Days")
plt.ylabel("Marks")
plt.show()