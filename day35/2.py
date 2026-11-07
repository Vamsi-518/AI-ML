
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
points = np.array([
    [1, 2],
    [2, 1],
    [2, 3],
    [8, 8],
    [9, 8],
    [8, 9]
])
RANDOM_STATE = 42
k_values = list(range(1, len(points) + 1))
inertias = []
for k in k_values:
    model = KMeans(
        n_clusters=k,
        n_init=10,
        random_state=RANDOM_STATE
    )
    model.fit(points)
    inertias.append(model.inertia_)
plt.plot(k_values, inertias, marker='o')
plt.title('Elbow Method (Toy Data)')
plt.xlabel('Number of Clusters K')
plt.ylabel('Inertia (Within-Cluster Sum of Squares)')
plt.xticks(k_values)
plt.grid(True)
plt.show()
