 # Day 16: Matplotlib

Matplotlib is a Python library used to create charts and visualizations.
This folder contains four basic chart examples:

- `line_plot.py`: shows a trend over time
- `bar_chat.py`: compares categories with vertical bars
- `horizontal_bar.py`: compares categories with horizontal bars
- `scatter_plot.py`: shows the relationship between two variables

## The Matplotlib Workflow

Every example follows the same basic process:

1. Import Matplotlib.
2. Prepare the data.
3. Choose a chart type.
4. Add a title and axis labels.
5. Display the chart.

```python
import matplotlib.pyplot as plt

# Prepare data
x_values = [1, 2, 3, 4, 5]
y_values = [60, 70, 75, 85, 90]

# Choose a chart type
plt.plot(x_values, y_values)

# Describe the chart
plt.title("Student Marks")
plt.xlabel("Days")
plt.ylabel("Marks")

# Display the chart
plt.show()
```

`pyplot` provides the plotting functions. The alias `plt` is the standard
convention. `plt.show()` opens the chart window.

## 1. Line Plot

File: `line_plot.py`

```python
days = [1, 2, 3, 4, 5]
marks = [60, 70, 75, 85, 90]

plt.plot(days, marks)
```

The first list supplies the x-axis values and the second list supplies the
y-axis values. Matplotlib connects the points with a line, making it easy to
see that the marks increase over the five days.

Use line plots for:

- Progress over time
- Temperature changes
- Sales trends
- Stock prices

## 2. Vertical Bar Chart

File: `bar_chat.py`

```python
students = ["Krishna", "Rahul", "vamsi", "Vinay"]
marks = [85, 72, 91, 65]

plt.bar(students, marks)
```

Each student is a category, and each bar height represents that student's
marks. Bar charts are useful for comparing separate categories.

Use bar charts for:

- Comparing student marks
- Comparing product sales
- Comparing department sizes
- Comparing counts by category

## 3. Horizontal Bar Chart

File: `horizontal_bar.py`

```python
students = ["Krishna", "Rahul", "Arjun", "Vijay"]
marks = [85, 72, 91, 65]

plt.barh(students, marks)
```

`plt.barh()` creates horizontal bars. The x-axis contains marks, the y-axis
contains student names, and the bar length represents each mark. Horizontal
bars are especially useful when category names are long.

## 4. Scatter Plot

File: `scatter_plot.py`

```python
age = [18, 19, 20, 21, 22, 23]
marks = [60, 65, 70, 75, 85, 90]

plt.scatter(age, marks)
```

Each matching pair creates one point:

```text
(18, 60), (19, 65), (20, 70), (21, 75), (22, 85), (23, 90)
```

This chart helps examine whether two variables are related. In this example,
the points suggest that marks increase as age increases.

Use scatter plots for:

- Age versus marks
- Advertising cost versus sales
- Height versus weight
- Study hours versus exam score

## Choosing the Right Chart

| Chart | Function | Best use |
| --- | --- | --- |
| Line plot | `plt.plot()` | Trends and changes |
| Vertical bar chart | `plt.bar()` | Category comparison |
| Horizontal bar chart | `plt.barh()` | Category comparison with readable labels |
| Scatter plot | `plt.scatter()` | Relationship between two variables |

## Titles, Labels, and Grid Lines

```python
plt.title("Chart Title")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.grid()
plt.show()
```

`title()` adds a chart title. `xlabel()` and `ylabel()` describe the axes.
`grid()` adds guide lines that make values easier to read.

Charts can also be styled:

```python
plt.bar(students, marks, color="skyblue")
plt.grid(axis="y")
```

The `color` argument changes the bar color. `grid(axis="y")` adds only
horizontal guide lines.

## Running the Examples

From the project root, run:

```powershell
python day16matplotlib/line_plot.py
python day16matplotlib/bar_chat.py
python day16matplotlib/horizontal_bar.py
python day16matplotlib/scatter_plot.py
```

If you are using the project's virtual environment:

```powershell
& .venv-1\Scripts\python.exe day16matplotlib/scatter_plot.py
```

The overall concept is:

```text
Data -> Select chart -> Add title and labels -> Display chart
```

Note: `bar_chat.py` appears to be named `bar_chat` instead of
`bar_chart`, but the filename does not prevent the program from running.
