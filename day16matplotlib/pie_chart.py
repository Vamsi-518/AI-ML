import matplotlib.pyplot as plt
subjects = ["Python", "SQL", "HTML", "CSS"]
hours = [5, 3, 2, 2]
plt.pie(hours, labels=subjects, autopct="%1.1f%%")
plt.title("Study Hours")
plt.show()