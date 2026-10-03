# Data Preprocessing

Data preprocessing is the process of cleaning and transforming raw data before using it in machine learning or data analysis. It helps the model learn better and makes the results more accurate and reliable.

In this folder, we cover the basic steps of preprocessing using Python and pandas:

- removing duplicate records
- handling missing values
- encoding categorical data
- scaling and standardizing features

## 1. Removing Duplicates

File: duplicates.py

Duplicate rows can create repeated information and affect the training process. We remove them using:

```python
 df = df.drop_duplicates()
```

This keeps only unique rows in the dataset.

Example:
- Same student appears twice with same details
- Duplicate data is removed so the dataset is more accurate

## 2. Handling Missing Values

File: missing_values.py

Missing values are common in real-world datasets. They can appear as `None`, `NaN`, or empty cells. We fill them using the mean of the column:

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

Why this is important:
- most machine learning algorithms cannot handle missing data directly
- missing values can break calculations or reduce model quality
- replacing them with a meaningful value keeps the dataset usable

## 3. Encoding Categorical Data

File: encoding.py

Some data is in text form, like `Male` and `Female`. Machine learning models usually work with numbers, so we convert categories into numeric values:

```python
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})
```

This is called encoding. It helps convert non-numeric data into a format the model can understand.

## 4. Feature Scaling

Files: feature_scaling.py and standradization.py

Different features may have different ranges, for example:
- Age ranges from 20 to 60
- Salary ranges from 20,000 to 80,000

If we use these values directly, some features may dominate the model because of their larger scale.

### Min-Max Scaling

Used in feature_scaling.py

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)
```

This transforms values into a range between 0 and 1.

### Standardization

Used in standradization.py

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df)
```

This converts data so it has mean 0 and standard deviation 1.

Why scaling matters:
- helps algorithms like KNN, SVM, and neural networks perform better
- prevents large value ranges from dominating small ones
- improves convergence during training

## 5. End-to-End Data Preprocessing Flow

The complete process is:

1. load raw data
2. remove duplicate rows
3. fill missing values
4. encode text labels to numbers
5. scale or standardize features
6. use cleaned data for training or analysis

This pipeline ensures the dataset is clean, consistent, and ready for machine learning models.

## Summary

Data preprocessing is one of the most important steps in machine learning. Without it, the model may learn from noisy, incomplete, or inconsistent data. These examples show the basic methods used to prepare data before training.

In short:
- clean the data
- fix missing values
- convert categories to numbers
- normalize feature scales
- build a better model
