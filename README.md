# task1
# Data Analysis and Visualization Using Pandas and Matplotlib

## 📌 Project Overview

This project demonstrates basic **data analysis and visualization** using Python libraries such as **Pandas** and **Matplotlib**.

The project uses a CSV dataset containing information about students, including their names, ages, and scores in different subjects. The data is analyzed to calculate averages and understand relationships between different variables through visualizations.

---

## 📂 Dataset

**File Name:** `student_data_300_students.csv`

The dataset contains information about **300 students**.

### Dataset Columns

| Column Name | Description         |
| ----------- | ------------------- |
| Name        | Name of the student |
| Age         | Age of the student  |
| Math        | Mathematics score   |
| Science     | Science score       |
| English     | English score       |

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib

---

## 📥 Installation

Install the required libraries using:

```bash id="d0tsw6"
pip install pandas matplotlib
```

---

## 📊 Data Analysis

The following basic data analysis tasks are performed using the Pandas library:

* Loading the CSV file
* Displaying the first few records
* Checking dataset information
* Generating summary statistics
* Calculating the average score of selected columns
* Analyzing the relationship between different numerical variables

### Loading the Dataset

```python id="i8mr4g"
import pandas as pd

df = pd.read_csv("student_data_300_students.csv")

print(df.head())
```

### Calculating Average Scores

```python id="uq9y2n"
average_math = df["Math"].mean()
average_science = df["Science"].mean()
average_english = df["English"].mean()

print("Average Math Score:", average_math)
print("Average Science Score:", average_science)
print("Average English Score:", average_english)
```

---

## 📈 Data Visualizations

The project includes the following visualizations using Matplotlib.

### 1. Bar Chart

A bar chart is used to compare the Math scores of students.

```python id="m7s5sv"
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.bar(df["Name"].head(10), df["Math"].head(10))

plt.title("Math Scores of Students")
plt.xlabel("Student Name")
plt.ylabel("Math Score")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
```

### 2. Scatter Plot

A scatter plot is used to analyze the relationship between Math and Science scores.

```python id="bf2m7l"
plt.figure(figsize=(8, 5))

plt.scatter(df["Math"], df["Science"])

plt.title("Relationship Between Math and Science Scores")
plt.xlabel("Math Score")
plt.ylabel("Science Score")

plt.show()
```

### 3. Heatmap

A heatmap is used to visualize the correlation between numerical columns.

```python id="z11y0c"
correlation = df[["Age", "Math", "Science", "English"]].corr()

plt.figure(figsize=(8, 6))

plt.imshow(correlation)
plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()
```

---

## 💡 Insights and Observations

The analysis and visualizations can provide the following insights:

* The average score helps understand the overall academic performance of students.
* The bar chart makes it easy to compare the scores of individual students.
* The scatter plot helps identify whether there is a relationship between Math and Science scores.
* Students who perform well in Math may also tend to perform well in Science if a positive trend is observed.
* The heatmap helps identify strong and weak correlations between Age and subject scores.
* A high positive correlation indicates that two variables tend to increase together.
* A correlation close to zero indicates little or no linear relationship.

---

## 🎯 Conclusion

This project demonstrates how **Pandas** can be used for loading and analyzing CSV data and how **Matplotlib** can be used to create meaningful visualizations.

The combination of data analysis and visualization helps in understanding patterns, relationships, and trends within the student performance dataset.

This project is useful for practicing:

* Data loading
* Data analysis
* Calculating averages
* Statistical analysis
* Bar chart visualization
* Scatter plot visualization
* Correlation analysis
* Heatmap visualization
