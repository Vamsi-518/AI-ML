
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from data_preprocessing import preprocess_data
def find_optimal_clusters():
    X_scaled, scaler = preprocess_data()
    inertia_values = []
    for k in range(1, 9):
        model = KMeans(
            n_clusters=k,
            init="k-means++",
            n_init=10,
            random_state=42
        )
        model.fit(X_scaled)
        inertia_values.append(model.inertia_)
        print(f"K = {k}, Inertia = {model.inertia_:.2f}")
    plt.plot(
        range(1, 9),
        inertia_values,
        marker="o"
    )
    plt.title("K-Means Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.xticks(range(1, 9))
    plt.grid(True)
    plt.show()
    return inertia_values
if __name__ == "__main__":
    find_optimal_clusters()
