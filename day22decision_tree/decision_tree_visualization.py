import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
X = [
    [1, 40], [2, 45], [3, 50], [4, 60],
    [5, 70], [6, 80], [7, 90], [8, 95]
]
y = [0, 0, 0, 0, 1, 1, 1, 1]
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)
model.fit(X, y)
plt.figure(figsize=(12, 7))
plot_tree(
    model,
    feature_names=["Hours", "Attendance"],
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True
)
plt.title("Decision Tree Classification")
plt.tight_layout()
plt.show()