import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("datasets\hospital.csv")
numerical = ["Procedure.Heart Attack.Cost", "Procedure.Heart Failure.Cost", "Procedure.Pneumonia.Cost", "Procedure.Hip Knee.Cost"]
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
