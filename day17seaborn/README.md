# Day 17 - Seaborn

Seaborn is a Python data visualization library built on top of Matplotlib. It is especially useful for statistical plots, data exploration, and making charts that look cleaner and easier to understand.

In this folder, we learn how to create different types of charts for different kinds of data questions.

---

## 1. What is Seaborn?

Seaborn helps us:

- visualize data quickly
- compare categories
- study distributions
- understand relationships between variables
- create clearer and more professional charts

The general pattern used in all scripts is:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# prepare data
# create chart
# set labels/title
# show chart
```

---

## 2. Basic setup used in every file

The scripts in this folder usually follow the same structure:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# data
# plot
plt.title("Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()
```

This means:

- `sns` is used to create the chart
- `plt` is used to format the chart
- `plt.show()` displays the final graph

---

## 3. Bar Plot

File: `bar_plot.py`

```python
students = ["Krishna", "Rahul", "Arjun", "Vijay"]
marks = [85, 72, 91, 65]
sns.barplot(x=students, y=marks)
```

### Purpose
This chart compares different categories using vertical bars.

### When to use
- compare marks of students
- compare sales across products
- compare performance across departments

### Meaning
Each bar represents one student and their marks.

---

## 4. Line Plot

File: `line_plot.py`

```python
days = [1, 2, 3, 4, 5]
marks = [60, 70, 75, 85, 90]
sns.lineplot(x=days, y=marks)
```

### Purpose
This chart shows change over time or in a sequence.

### When to use
- increase in marks over days
- sales over months
- temperature changes over time

### Meaning
The line connects points in order, which helps us see trends and patterns.

---

## 5. Scatter Plot

File: `scatter_plot.py`

```python
age = [18, 19, 20, 21, 22, 23]
marks = [60, 65, 70, 75, 85, 90]
sns.scatterplot(x=age, y=marks)
```

### Purpose
This chart shows the relationship between two numeric variables.

### When to use
- age vs marks
- height vs weight
- study hours vs score

### Meaning
Each point is a pair of values. If the points move together, there may be a relationship between the variables.

---

## 6. Histogram

File: `histogram.py`

```python
marks = [45, 50, 55, 60, 65, 65, 70, 75, 80, 85, 90, 95]
sns.histplot(marks, bins=5)
```

### Purpose
This chart shows how data is distributed across ranges or bins.

### When to use
- frequency of marks
- age distribution
- income distribution

### Meaning
The bars show how many values fall in each range.

---

## 7. Distribution Plot (KDE)

File: `distribution_plot.py`

```python
marks = [45, 50, 55, 60, 65, 65, 70, 75, 80, 85, 90, 95]
sns.kdeplot(marks, fill=True)
```

### Purpose
A KDE plot shows the smooth curve of a distribution.

### When to use
- understand the overall shape of the data
- compare density of values
- visualize probability patterns

### Meaning
A wider section of the curve means more data is concentrated there.

---

## 8. Box Plot

File: `box_plot.py`

```python
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
sns.boxplot(y=marks)
```

### Purpose
A box plot summarizes the spread and center of data.

### What it shows
- median = middle value
- box = middle 50% of data
- whiskers = spread
- outliers = unusual values

### When to use
- compare performance ranges
- identify outliers
- understand data spread quickly

---

## 9. Violin Plot

File: `violin_plot.py`

```python
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
sns.violinplot(y=marks)
```

### Purpose
A violin plot combines a density curve with a box-like summary.

### When to use
- understand distribution of values deeply
- compare data distribution visually

### Meaning
The width of the violin at different points represents how many values are around that range.

---

## 10. Count Plot

File: `count_plot.py`

```python
courses = ["Python", "Java", "Python", "SQL", "Python", "Java"]
sns.countplot(x=courses)
```

### Purpose
This chart counts how many times each category appears.

### When to use
- count students in each course
- count votes in each category
- count product sales by type

### Meaning
It tells us the frequency of each category.

---

## 11. Heatmap

File: `heatmap.py`

```python
data = [
    [85, 90, 80],
    [70, 75, 72],
    [91, 88, 95]
]
sns.heatmap(data, annot=True)
```

### Purpose
A heatmap shows values in a matrix using colors.

### When to use
- compare marks across subjects
- show correlation tables
- represent performance by rows and columns

### Meaning
Dark or light colors represent high or low values. `annot=True` writes the actual values in each cell.

---

## 12. Pair Plot

File: `pair_plot.py`

```python
data = sns.load_dataset("iris")
sns.pairplot(data)
```

### Purpose
Pair plot compares every numeric feature against every other numeric feature.

### When to use
- exploratory data analysis (EDA)
- finding relationships between many variables
- understanding how features interact

### Meaning
It creates a grid of scatter plots and helps us quickly inspect patterns in the dataset.

---

## 13. End-to-End Summary

This day teaches the main idea of Seaborn:

1. Prepare your data.
2. Choose the correct plot based on the data and question.
3. Use Seaborn functions to draw the chart.
4. Add labels and titles for clarity.
5. Display the chart with `plt.show()`.

The key chart types in this lesson are:

- Bar plot – comparison
- Line plot – trend over time
- Scatter plot – relationship between two variables
- Histogram – distribution/frequency
- KDE plot – smooth density curve
- Box plot – summary and outliers
- Violin plot – distribution shape
- Count plot – category counts
- Heatmap – matrix/values comparison
- Pair plot – multiple variable relationships

---

## 14. Why Seaborn is important

Seaborn is important because it makes data analysis visual and easier to understand. In real projects, charts help us:

- identify patterns
- detect outliers
- understand distributions
- compare categories
- explain data insight clearly

This is a very important step before building machine learning models or making data-driven decisions.

---

## 15. Final takeaway

Day 17 is about learning how to represent data visually using Seaborn.

By the end of this lesson, you should be able to:

- choose the right plot for the right task
- use Seaborn functions correctly
- read charts meaningfully
- explain data patterns using visuals

This is one of the most practical parts of data science and analytics because visualizations help people understand data faster than raw numbers alone.
