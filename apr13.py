import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("hospital.csv")
numerical = ["Procedure.Heart Attack.Cost", "Procedure.Heart Failure.Cost", "Procedure.Pneumonia.Cost", "Procedure.Hip Knee.Cost"]
values = data[numerical]

mean = values.mean()
sem = values.sem()
confidence = 0.90
ci = stats.t.interval(confidence, len(values) - 1, loc=mean, scale=sem)

print("Mean value \n", mean)
print("Standard Error \n", sem)
print("Confidence Interval \n", ci)

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
for i, column in enumerate(numerical):
    ax = axs[i // 2, i % 2]
    ax.axhline(mean[column], color="green", linestyle="--", label="Mean")
    ax.fill_between([0, 1], ci[0][i], ci[1][i], color="lightblue", alpha=0.5, label=f"{confidence*100}% confidence interval")
    ax.set_xlim(0, 1)
    ax.set_ylim(values[column].min() - 50, values[column].max() + 50)
    ax.legend()
    ax.set_title(column)

plt.tight_layout()
plt.show()
