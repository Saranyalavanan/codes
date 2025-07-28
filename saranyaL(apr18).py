import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, zscore
from scipy import stats

data = pd.read_csv("crime_data.csv")
meanvalue = pd.DataFrame({
    'metric': ["Year", "Total Cognizable IPC crimes"],
    'mean': [data["Year"].mean(), data["Total Cognizable IPC crimes"].mean()]
})

plt.figure(figsize=(8, 6))
sns.barplot(x='metric', y='mean', data=meanvalue, palette='viridis')
plt.title("Mean of Year and Total Cognizable IPC crimes")
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
        print(f"{col} has heavy tails")
    elif k < 0:
        print(f"{col} has light tails")
    else:
        print(f"{col} has normal tails")


plt.figure(figsize=(12, 6))
sns.barplot(x=skewness.index, y=skewness.values, palette="coolwarm")
plt.xticks(rotation=90)
plt.title("Skewness of Numerical Columns")
plt.xlabel("Feature")
plt.ylabel("Skewness")
plt.tight_layout()
plt.show()

sample = data['Year']
data["zscore"] = zscore(sample)
print(data)


numerical = ["Year", "Total Cognizable IPC crimes"]
confidence = 0.99

for column in numerical:
    values = data[column].dropna()
    mean = np.mean(values)
    sem = stats.sem(values)
    ci = stats.t.interval(confidence, len(values) - 1, loc=mean, scale=sem)
    l, u = ci

print(f"column : {column}")
print(f"mean value : {mean}")
print(f"satandard Error : {sem}")
print(f"confidence interval : {ci}")
print()


plt.figure(figsize=(8, 6))
plt.axhline(mean, color="brown", linestyle="--", label="Mean")
plt.fill_between([0, 1], l, u, color="lightblue", alpha=0.5,label=f"{int(confidence * 100)}% Confidence Interval")
plt.xlim(0, 1)
plt.ylim(min(values) - 50, max(values) + 50)
plt.title(f"{column} with {int(confidence*100)}% Confidence Interval")
plt.legend()
plt.show()


numerical = ["Attempt to commit Murder","Rape"]
values = data[numerical]
mean = values.mean()
std = values.std()
z_scores = (values - mean) / std
print(mean,std,values,z_scores,sep="\n")

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(data=values.melt(), x="value", hue="variable", kde=True, palette="RdBu")
plt.title("Original Data Distribution")

plt.subplot(1, 2, 2)
sns.histplot(data=z_scores.melt(), x="value", hue="variable", kde=True, palette="pastel")
plt.title("Z-score Normalized Distribution")

plt.tight_layout()
plt.show()
