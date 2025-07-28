import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("hospital.csv")
numerical = ["Procedure.Heart Attack.Cost", "Procedure.Heart Failure.Cost", "Procedure.Pneumonia.Cost", "Procedure.Hip Knee.Cost"]
values = data[numerical]
confidence = 0.90


for column in numerical:
    mean = np.mean(values[column])
    sem = stats.sem(values[column])
    ci = stats.t.interval(confidence, len(values[column]) - 1, loc=mean, scale=sem)
    l, u = ci
    
    print(f"Column: {column}")
    print(f"Mean value: {mean}")
    print(f"Standard Error: {sem}")
    print(f"Confidence Interval: {ci}")
    print()

    plt.figure(figsize=(8, 6))
    plt.axhline(mean, color="brown", linestyle="--", label="Mean")
    plt.fill_between([0, 1], l, u, color="lightblue", alpha=0.5, label=f"{confidence*100}% confidence interval")
    plt.xlim(0, 1)
    plt.ylim(min(values[column]) - 50, max(values[column]) + 50)
    plt.legend()
    plt.title(column)
    plt.show()
