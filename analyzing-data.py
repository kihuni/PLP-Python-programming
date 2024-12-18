# Task 1: Load and Explore the Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"  # Iris dataset in CSV format
df = pd.read_csv(url)

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset (if missing values exist)
if df.isnull().sum().any():
    # Drop rows with missing values (alternatively, you could fill them)
    df = df.dropna()

print("\nData after cleaning:")
print(df.info())


# Task 2: Basic Data Analysis

# Basic statistics for numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Grouping by the 'species' column and computing the mean of numerical columns
grouped = df.groupby('species').mean()
print("\nMean values by species:")
print(grouped)

# Task 3: Data Visualization

# Set a theme for seaborn plots
sns.set_theme()

# Example: cumulative sum of petal_length
df['cumulative_petal_length'] = df['petal_length'].cumsum()

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['cumulative_petal_length'], label="Cumulative Petal Length", color='blue')
plt.title("Cumulative Petal Length Over Observations")
plt.xlabel("Index")
plt.ylabel("Cumulative Petal Length")
plt.legend()
plt.show()

# Average petal length per species
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df, palette='viridis')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length")
plt.show()

# Histogram of petal_length
plt.figure(figsize=(8, 6))
sns.histplot(df['petal_length'], bins=20, kde=True, color='green')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.show()


# Scatter plot of sepal_length vs petal_length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df, palette='deep')
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend(title="Species")
plt.show()
