
import pandas as pd
def load_dataset():
    data = {
        "CustomerID": range(1, 16),
        "Annual_Income": [
            15, 16, 17, 18, 20,
            35, 36, 38, 40, 42,
            60, 65, 70, 75, 80
        ],
        "Spending_Score": [
            80, 85, 78, 82, 88,
            40, 45, 38, 42, 48,
            20, 25, 18, 22, 28
        ]
    }
    df = pd.DataFrame(data)
    print("Customer dataset loaded!")
    print(df.head())
    return df
if __name__ == "__main__":
    load_dataset()
