import seaborn as sns
import matplotlib.pyplot as plt
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
sns.boxplot(y=marks)
plt.title("Marks Box Plot")
plt.ylabel("Marks")
plt.show()