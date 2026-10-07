import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 45, 50, 60, 70, 80]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
model = LinearRegression()
model.fit(X, y)
hours = [[7]]
prediction = model.predict(hours)
print("Student Study Hours:", hours[0][0])
print("Predicted Marks:", prediction[0])