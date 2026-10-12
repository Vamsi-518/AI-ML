from sklearn.tree import DecisionTreeClassifier
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)
model.fit(X, y)
print("Decision Tree Classifier Created!")
print("Tree Depth:", model.get_depth())
print("Number of Leaves:", model.get_n_leaves())
print("Classes:", model.classes_)