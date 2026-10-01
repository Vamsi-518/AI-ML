import seaborn as sns
import matplotlib.pyplot as plt
marks = [45, 50, 55, 60, 65, 65, 70, 75, 80, 85, 90, 95]
sns.histplot(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()