
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)
print("Gradient Boosting Classifier")
print(model)
print("\nModel created successfully!")
