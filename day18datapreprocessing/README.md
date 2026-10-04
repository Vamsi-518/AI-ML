# Day 18: Data Preprocessing

This folder shows how to prepare data before machine learning:

- `normalization.py` scales marks to a 0-to-1 range.
- `outliers.py` finds unusual marks using the IQR method.
- `train_test_split.py` divides data into training and testing sets.
- `feature_selection.py` separates input features from the target.
- `preprocessing_pipeline.py` combines these steps in one example.

## End-to-end program

Run from the project root:

```powershell
python day18datapreprocessing\preprocessing_pipeline.py
```

The program creates sample student data, selects `Age`, `Marks`, and `Height` as
features, and uses `Result` as the target. It splits the rows into training and test
sets, caps outliers using limits calculated from the training data, then normalizes
the features with `MinMaxScaler`. Finally, it prints the processed data and labels.

The split happens before outlier handling and normalization so that test data does
not influence the preprocessing values learned from training data.
