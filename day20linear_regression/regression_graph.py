import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 45, 50, 60, 70, 75, 85, 90]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual vs Predicted Marks")
plt.show()