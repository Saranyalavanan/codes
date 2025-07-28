import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew,kurtosis,zscore
from scipy import stats

data = pd.read_csv("datasets\detailed_data.csvdetailed_data.csv")
mean_value = {
    'metric': ["year", "Salary"],
    'mean': [data["year"].mean(), data["Salary"].mean()]
}

plt.figure(figsize=(8, 6))
sns.barplot(x='metric', y='mean', data=mean_value, palette='viridis')
plt.title("Mean of Year and Salary")
plt.xlabel('Metric')
plt.ylabel('Mean')
plt.show()

numdata = data.select_dtypes(include=["number"])
skewness = numdata.apply(skew)
print("Skewness information")

for col, skews in skewness.items():
    if skews > 0:
        print(f"{col} is positively skewed")
    elif skews < 0:
        print(f"{col} is negatively skewed")
    else:
        print(f"{col} is normally distributed")
print("--------------------------------------------------------")
kurt = numdata.apply(kurtosis)
print("Kurtosis information")
for col, k in kurt.items():
    if k > 0:
        print(f"{col} this is heavily tails")
    elif k < 0:
        print(f"{col} this is lightly tails")
    else:
        print(f"{col} normal tails")

plt.figure(figsize=(10, 6))
sns.barplot(x=skewness.index, y=skewness.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Skewness of Numerical Columns")
plt.xlabel("Feature")
plt.ylabel("Skewness")
plt.tight_layout()
plt.show()

sample = data["Salary"]
data["zscore"] = zscore(sample)
print(data)

numerical = ["year","Salary"]
values = data[numerical]
confidence = 0.90
for column in numerical:
    mean = np.mean(values[column])
    sem = stats.sem(values[column])
    ci = stats.t.interval(confidence, len(values[column]) - 1, loc=mean, scale=sem)
    l,u = ci
print(f"column : {column}")
print(f"mean value : {mean}")
print(f"satandard Error : {sem}")
print(f"confidence interval : {ci}")
print()

plt.figure(figsize=(8, 6))
plt.axhline(mean, color="brown", linestyle="--", label="Mean")
plt.fill_between([0, 1], l, u, color="lightblue", alpha=0.5, label=f"{confidence*100}% confidence interval")
plt.xlim(0, 1)
plt.ylim(min(values[column]) - 50, max(values[column]) + 50)
plt.legend()
plt.title(column)
plt.show()

numerical = ["year","Salary"]
values = data[numerical]

mean = values.mean()
std = values.std()
z_scores = (values - mean) / std
print(mean,std,values,z_scores,sep="\n")

plt.subplot(1, 2, 1)
sns.histplot(data=values.melt(), x="value", hue="variable", kde=True, palette="RdBu")
plt.subplot(1, 2, 2)
sns.histplot(data=z_scores.melt(), x="value", hue="variable", kde=True, palette="pastel")
plt.show()




