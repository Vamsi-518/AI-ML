from sklearn.metrics import r2_score
actual = [50, 60, 70, 80]
predicted = [48, 62, 68, 82]
score = r2_score(actual, predicted)
print("Actual Values:")
print(actual)
print("\nPredicted Values:")
print(predicted)
print("\nR2 Score:")
print(score)