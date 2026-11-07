import numpy as np
points = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])
centroids = np.array([
    [2, 3],
    [6, 7]
])
print("Shape of points:", points.shape)          
print("Shape of centroids:", centroids.shape)    
print("\nShape after adding new axes:")
print("Points:", points[:, None, :].shape)       
print("Centroids:", centroids[None, :, :].shape)  
diff = points[:, None, :] - centroids[None, :, :]
print("\nDifference between points and centroids:")
print(diff)
distances = np.linalg.norm(diff, axis=2)
print("\nDistance matrix:")
print(distances)
labels = distances.argmin(axis=1)
print("\nCluster assignments:")
print(labels)