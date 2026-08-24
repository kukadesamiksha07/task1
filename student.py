import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("student.csv")

print("Dataset: ")
print(df.head())

print("\n Dataset Information: ")
print(df.info())

print("\n Summary Statistics: ")
print(df.describe())

avg_math = df["Math"].mean()
print(f"\nAverage math score : {avg_math:.2f}")

plt.figure(figsize=(8,5))
plt.bar(df["Name"],df["Math"])
plt.title("Math Scores Of Students")
plt.xlabel("Students")
plt.ylabel("Math Score")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df["Math"],df["Science"])
plt.title("Math vs Science Scores")
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.show()

correlation = df[["Age", "Math", "Science", "English"]].corr()

plt.figure(figsize=(6,5))
plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.title("correlation Heatmap")

for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(j,i,
                 f"{correlation.iloc[i,j]:.2f}",
                 ha="center",
                 va="center",
                 color="black")

plt.tight_layout()
plt.show()
