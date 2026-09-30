import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
marks = [60, 65, 75, 80, 90]
plt.fill_between(days, marks)
plt.title("Progress")
plt.xlabel("Days")
plt.ylabel("Marks")
plt.show()