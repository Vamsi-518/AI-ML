from sklearn.metrics import mean_squared_error
actual = [50, 60, 70, 80]
predicted = [48, 62, 68, 82]
mse = mean_squared_error(actual, predicted)
print("Actual Values:")
print(actual)
print("\nPredicted Values:")
print(predicted)
print("\nMean Squared Error:")
print(mse)