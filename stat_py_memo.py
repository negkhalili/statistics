# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 18:19:03 2023

@author: user
"""

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import pearsonr, chi2_contingency

# Load data
df = pd.read_csv("data.csv")

# T-test
group1 = df[df["group"] == 1]["score"]
group2 = df[df["group"] == 2]["score"]
t_stat, p_val = ttest_ind(group1, group2)
print("T-test result: t = {:.2f}, p-value = {:.3f}".format(t_stat, p_val))

# Scatter plot
plt.scatter(x = df["weight"], y = df["mpg"])
plt.title("MPG vs. Weight")
plt.xlabel("Weight (1000 lbs)")
plt.ylabel("Miles per Gallon")
plt.show()

# Histogram
sns.histplot(df["mpg"], kde = True, color = "lightblue")
plt.title("MPG Distribution")
plt.xlabel("Miles per Gallon")
plt.ylabel("Frequency")
plt.show()

# Box plot
sns.boxplot(x = "cyl", y = "mpg", data = df, color = "lightblue")
plt.title("MPG by Number of Cylinders")
plt.xlabel("Number of Cylinders")
plt.ylabel("Miles per Gallon")
plt.show()

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Bar plot
counts = df["cyl"].value_counts()
plt.bar(counts.index, counts.values, color = "lightblue")
plt.title("Number of Cars by Number of Cylinders")
plt.xlabel("Number of Cylinders")
plt.ylabel("Number of Cars")
plt.show()

# Scatter plot with regression line
sns.regplot(x = "weight", y = "mpg", data = df)
plt.title("MPG vs. Weight with Regression Line")
plt.xlabel("Weight (1000 lbs)")
plt.ylabel("Miles per Gallon")
plt.show()




# Load data
df = pd.read_csv("data.csv")

# Pearson correlation test
corr, p_val = pearsonr(df["weight"], df["mpg"])
print("Pearson correlation test result: correlation = {:.2f}, p-value = {:.3f}".format(corr, p_val))

# Violin plot
sns.violinplot(x = "cyl", y = "mpg", data = df, color = "lightblue")
plt.title("MPG by Number of Cylinders")
plt.xlabel("Number of Cylinders")
plt.ylabel("Miles per Gallon")
plt.show()

# Pie chart
counts = df["cyl"].value_counts()
plt.pie(counts.values, labels = counts.index, colors = ["lightblue", "lightgreen", "pink"], autopct = "%.1f%%")
plt.title("Number of Cars by Number of Cylinders")
plt.show()

# Heatmap
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot = True, cmap = "coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Bar plot with error bars
means = df.groupby("cyl")["mpg"].mean()
stds = df.groupby("cyl")["mpg"].std()
plt.bar(means.index, means.values, yerr = stds.values, color = "lightblue")
plt.title("MPG by Number of Cylinders")
plt.xlabel("Number of Cylinders")
plt.ylabel("Miles per Gallon")
plt.show()

# Chi-squared test
contingency_table = pd.crosstab(df["cyl"], df["am"])
chi_stat, p_val, dof, expected = chi2_contingency(contingency_table)
print("Chi-squared test result: chi-square = {:.2f}, p-value = {:.3f}".format(chi_stat, p_val))
