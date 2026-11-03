from sklearn.cluster import DBSCAN
def create_model(eps=0.25, min_samples=5):
    model = DBSCAN(
        eps=eps,
        min_samples=min_samples
    )
    print("DBSCAN model created!")
    return model
if __name__ == "__main__":
    create_model()