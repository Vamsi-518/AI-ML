
import pandas as pd
import matplotlib.pyplot as plt

from model_training import train_model


def show_feature_importance():
    model, X_train, X_test, y_train, y_test = train_model()

    importance = pd.Series(
        model.feature_importances_,
        index=X_train.columns
    ).sort_values(ascending=False)

    print("\nFeature Importance:")
    print(importance)

    importance.sort_values().plot(
        kind="barh",
        title="XGBoost Feature Importance"
    )

    plt.xlabel("Importance Score")
    plt.tight_layout()
    plt.show()

    return importance


if __name__ == "__main__":
    show_feature_importance()
