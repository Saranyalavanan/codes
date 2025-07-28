import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, zscore
from scipy import stats

# Load data
data = pd.read_csv("datasets/detailed_data.csv")

# Mean plot
mean_value = pd.DataFrame({
    'metric': ["year", "Salary"],
    'mean': [data["year"].mean(), data["Salary"].mean()]
})

plt.figure(figsize=(8, 6))
sns.barplot(x='metric', y='mean', data=mean_value, palette='viridis')
plt.title("Mean of Year and Salary")
plt.xlabel('Metric')
plt.ylabel('Mean')
plt.show()

# Skewness
numdata = data.select_dtypes(include=["number"])
skewness = numdata.apply(skew)
print("Skewness Information:")
for col, skews in skewness.items():
    if skews > 0:
        print(f"{col} is positively skewed")
    elif skews < 0:
        print(f"{col} is negatively skewed")
    else:
        print(f"{col} is normally distributed")

print("--------------------------------------------------------")

# Kurtosis
kurt = numdata.apply(kurtosis)
print("Kurtosis Information:")
for col, k in kurt.items():
    if k > 0:
        print(f"{col} has heavy tails")
    elif k < 0:
        print(f"{col} has light tails")
    else:
        print(f"{col} has normal tails")

# Skewness barplot
plt.figure(figsize=(10, 6))
sns.barplot(x=skewness.index, y=skewness.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Skewness of Numerical Columns")
plt.xlabel("Feature")
plt.ylabel("Skewness")
plt.tight_layout()
plt.show()

# Z-score for Salary
data["zscore"] = zscore(data["Salary"])
print(data[["Salary", "zscore"]].head())

# Confidence Intervals for Numerical Columns
numerical = ["year", "Salary"]
values = data[numerical]
confidence = 0.90

for column in numerical:
    mean = np.mean(values[column])
    sem = stats.sem(values[column])
    ci = stats.t.interval(confidence, len(values[column]) - 1, loc=mean, scale=sem)
    l, u = ci

    print(f"Column: {column}")
    print(f"Mean Value: {mean}")
    print(f"Standard Error: {sem}")
    print(f"{int(confidence*100)}% Confidence Interval: {ci}")
    print()

    # Confidence interval plot
    plt.figure(figsize=(8, 6))
    plt.axhline(mean, color="brown", linestyle="--", label="Mean")
    plt.fill_between([0, 1], l, u, color="lightblue", alpha=0.5, label=f"{int(confidence*100)}% confidence interval")
    plt.xlim(0, 1)
    plt.ylim(min(values[column]) - 50, max(values[column]) + 50)
    plt.legend()
    plt.title(f"{column} with Confidence Interval")
    plt.ylabel(column)
    plt.show()

# Standardizing
mean = values.mean()
std = values.std()
z_scores = (values - mean) / std

print("Raw Means:\n", mean)
print("Standard Deviations:\n", std)
print("Original Values:\n", values.head())
print("Z-Scores:\n", z_scores.head())

# Histograms of raw and standardized data
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(data=values.melt(), x="value", hue="variable", kde=True, palette="RdBu")
plt.title("Original Data Distribution")

plt.subplot(1, 2, 2)
sns.histplot(data=z_scores.melt(), x="value", hue="variable", kde=True, palette="pastel")
plt.title("Standardized Data (Z-Scores)")
plt.tight_layout()
plt.show()
