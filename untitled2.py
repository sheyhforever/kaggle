# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sllqcGCOn6agcD6mLBnIxiKpWJI7oqwl
"""

# Import necessary libraries
import pandas as pd

# Load the dataset (ensure the file is uploaded to /content)
file_path = "/content/Turkiye_National_Team_Dataset_English_1.csv"  # Update with your actual file name if different
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"File not found at {file_path}. Please upload the dataset to the correct path.")

# Display the first 5 rows of the dataset
print("\nPreview of the dataset:")
print(data.head())

# Display information about the dataset
print("\nDataset Info:")
print(data.info())

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Display column names
print("\nColumn Names:")
print(data.columns)

# Optional: Visualize correlations (if numerical data exists)
import seaborn as sns
import matplotlib.pyplot as plt

print("\nCorrelation Heatmap:")
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()