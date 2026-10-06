from sklearn.linear_model import LinearRegression
import joblib
X = [[1], [2], [3], [4], [5], [6]]
y = [35, 45, 50, 60, 70, 80]
model = LinearRegression()
model.fit(X, y)
joblib.dump(model, "student_marks_model.pkl")
print("Model saved successfully!")
print("File: student_marks_model.pkl")