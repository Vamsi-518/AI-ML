import matplotlib.pyplot as plt
from dimensionality_reduction import reduce_dimensions
def visualize_pca():
    df = reduce_dimensions()
    plt.figure(figsize=(9, 6))
    for target in sorted(df["target"].unique()):
        subset = df[df["target"] == target]
        plt.scatter(
            subset["Principal_Component_1"],
            subset["Principal_Component_2"],
            label=f"Class {target}"
        )
    plt.title("Iris Dataset After PCA")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    visualize_pca()