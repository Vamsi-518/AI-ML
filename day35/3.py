import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
# Step 1: Create sample data
points = np.array([
    [1, 2],
    [2, 1],
    [2, 3],
    [8, 8],
    [9, 8],
    [8, 9]
])
RANDOM_STATE = 42
# Step 2: Elbow Method
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
# Display Elbow graph
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertias, marker='o')
plt.title('Elbow Method (Toy Data)')
plt.xlabel('Number of Clusters K')
plt.ylabel('Inertia (Within-Cluster Sum of Squares)')
plt.xticks(k_values)
plt.grid(True)
plt.show()
# Step 3: Silhouette Score
sil_k_values = list(range(2, len(points)))
sil_scores = []
for k in sil_k_values:
    labels_k = KMeans(
        n_clusters=k,
        n_init=10,
        random_state=RANDOM_STATE
    ).fit_predict(points)
    score = metrics.silhouette_score(points, labels_k)
    sil_scores.append(score)
# Step 4: Create Silhouette Table
silhouette_table = pd.DataFrame({
    'K': sil_k_values,
    'silhouette': sil_scores
})
print("\nSilhouette Score Table:")
print(silhouette_table.to_string(index=False))
# Step 5: Find Best K
best_k_toy = sil_k_values[int(np.argmax(sil_scores))]
print("\nK with the highest silhouette:", best_k_toy)
# Step 6: Display Silhouette Graph
plt.figure(figsize=(8, 5))
plt.plot(
    sil_k_values,
    sil_scores,
    marker='o',
    color='green'
)
plt.title('Silhouette Score by K (Toy Data)')
plt.xlabel('Number of Clusters K')
plt.ylabel('Average Silhouette')
plt.xticks(sil_k_values)
plt.grid(True)
plt.show()
