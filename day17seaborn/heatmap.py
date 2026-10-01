import seaborn as sns
import matplotlib.pyplot as plt
data = [
    [85, 90, 80],
    [70, 75, 72],
    [91, 88, 95]
]
sns.heatmap(data, annot=True)
plt.title("Student Marks Heatmap")
plt.show()