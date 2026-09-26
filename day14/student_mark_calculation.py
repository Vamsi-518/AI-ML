import numpy as np
students = np.array([
    [85, 90, 80],
    [70, 75, 80],
    [95, 90, 92]
])
print("Total:", np.sum(students))
print("Average:", np.mean(students))
print("Highest:", np.max(students))
print("Lowest:", np.min(students))